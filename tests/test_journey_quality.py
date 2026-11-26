"""Dependency-free source-contract tests for the first-win journeys."""

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".github" / "scripts"))
from check_journey_quality import StepText, audit, check_events, check_route  # noqa: E402


def task(slug="dinner"):
    return (ROOT / "products" / "landing" / f"{slug}.html").read_text(encoding="utf-8")


def script():
    return (ROOT / "products" / "landing" / "assets" / "entry.js").read_text(encoding="utf-8")


class JourneyQualityTests(unittest.TestCase):
    def test_current_published_journeys_pass_without_visiting_the_site(self):
        report, problems = audit(ROOT)
        self.assertEqual(problems, [])
        self.assertEqual(report["status"], "PASS")
        self.assertEqual(len(report["routes"]), 6)
        self.assertEqual(sum(r["placement"] == "public-picker" for r in report["routes"]), 5)
        self.assertEqual(sum(r["placement"] == "direct-link-only" for r in report["routes"]), 1)
        self.assertTrue(all(r["step_count"] == 6 for r in report["routes"]))
        self.assertEqual(len(report["events"]), 13)
        self.assertIn("not proof of physical task completion", report["measurement_limit"])

    def test_step_parser_recovers_action_and_heading(self):
        parsed = StepText()
        parsed.feed(task())
        self.assertEqual(len(parsed.steps), 6)
        self.assertEqual(parsed.steps[0]["heading"], "Throw away the obvious trash.")
        self.assertIn("Take wrappers", parsed.steps[0]["action"])

    def test_missing_step_stops_the_line(self):
        broken = task().replace('<li class="step">', '<li class="invisible">', 1)
        _, problems = check_route("dinner", "dinner.html", "finished-dinner.html", broken,
                                  in_public_picker=True)
        self.assertTrue(any("5 action steps" in p for p in problems), problems)

    def test_empty_action_stops_the_line(self):
        source = task()
        source = source.replace('<p class="do">Take wrappers, empty packaging, and other obvious trash off the table and into a bag. Leave anything you need to think about for step four.</p>',
                                '<p class="do">  </p>', 1)
        _, problems = check_route("dinner", "dinner.html", "finished-dinner.html", source,
                                  in_public_picker=True)
        self.assertTrue(any("step 1 has no action" in p for p in problems), problems)

    def test_completion_identity_drift_stops_the_line(self):
        source = task().replace('data-completion-url="/finished-dinner.html"',
                                'data-completion-url="/finished-guests.html"', 1)
        _, problems = check_route("dinner", "dinner.html", "finished-dinner.html", source,
                                  in_public_picker=True)
        self.assertTrue(any("completion path mismatch" in p for p in problems), problems)

    def test_replaced_finished_event_is_detected(self):
        source = script().replace("track('finished'", "notTrack('finished'", 1)
        _, problems = check_events(source)
        self.assertTrue(any("missing event 'finished'" in p for p in problems), problems)

    def test_event_with_personal_identifier_is_rejected(self):
        source = script() + "\ntrack('start-now', {email: 'person@example.com'});\n"
        _, problems = check_events(source)
        self.assertTrue(any("unreviewed payload keys ['email']" in p for p in problems), problems)

    def test_unreviewed_new_event_is_rejected(self):
        source = script() + "\ntrack('purchase', {});\n"
        _, problems = check_events(source)
        self.assertTrue(any("unexpected analytics event 'purchase'" in p for p in problems), problems)

    def test_nested_payload_cannot_bypass_event_key_review(self):
        source = script() + "\ntrack('start-now', {visitor: {email: 'private'}});\n"
        _, problems = check_events(source)
        self.assertTrue(any('unreviewed analytics track() call shape' in p for p in problems), problems)

    def test_computed_event_name_cannot_bypass_event_review(self):
        source = script() + "\nconst eventName = 'purchase'; track(eventName, {});\n"
        _, problems = check_events(source)
        self.assertTrue(any('unreviewed analytics track() call shape' in p for p in problems), problems)

    def test_direct_umami_call_cannot_bypass_event_review(self):
        source = script() + "\nwindow.umami.track('purchase', {email: 'private'});\n"
        _, problems = check_events(source)
        self.assertTrue(any('direct Umami tracking bypasses' in p for p in problems), problems)

    def test_event_key_cannot_be_repurposed_in_a_different_stage(self):
        source = script() + "\ntrack('start-now', {step: '6'});\n"
        _, problems = check_events(source)
        self.assertTrue(any("start-now has unreviewed payload keys ['step']" in p for p in problems), problems)

    def test_ternary_value_is_not_mistaken_for_a_payload_key(self):
        _, problems = check_events(script())
        self.assertEqual(problems, [])


if __name__ == "__main__":
    unittest.main()
