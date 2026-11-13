"""Mobile integration checks. Run after build_site.py; requires Python Playwright.
CAMPAIGN_BROWSER can select a Chromium executable. No external requests or saves.
"""
import functools
import http.server
import os
from pathlib import Path
import shutil
import threading
import unittest
from datetime import datetime
from urllib.parse import unquote, urlsplit, parse_qs
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
NOW = datetime.fromisoformat('2026-11-13T00:00:00+00:00')  # 5pm in Boise

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *_args):
        pass

class CampaignFlows(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(QuietHandler, directory=str(ROOT / '_site')))
        threading.Thread(target=cls.server.serve_forever, daemon=True).start()
        cls.origin = 'http://127.0.0.1:' + str(cls.server.server_port)
        cls.playwright = sync_playwright().start()
        shells = list((ROOT / 'video/node_modules/.remotion').glob('**/chrome-headless-shell'))
        executable = os.environ.get('CAMPAIGN_BROWSER') or next((str(p) for p in shells if p.is_file()), None) or shutil.which('chromium')
        cls.browser = cls.playwright.chromium.launch(executable_path=executable, args=['--no-sandbox'])

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.playwright.stop()
        cls.server.shutdown()
        cls.server.server_close()

    def setUp(self):
        self.context = self.browser.new_context(viewport={'width': 390, 'height': 844}, timezone_id='America/Boise')
        self.context.route('**/*', lambda r: r.continue_() if r.request.url.startswith(self.origin) else r.abort())
        self.page = self.context.new_page()
        self.errors = []
        self.page.on("pageerror", lambda error: self.errors.append(str(error)))
        self.page.clock.install(time=NOW)

    def tearDown(self):
        self.context.close()
        self.assertEqual(self.errors, [])

    def open_task(self, slug='guests', query=''):
        self.page.goto(self.origin + '/' + slug + '.html' + query)

    def start_checklist(self):
        self.page.locator('.go-do').click()
        self.assertTrue(self.page.locator('.frame').is_visible())
        self.assertTrue(self.page.locator('.steps').is_hidden())
        self.page.locator('.prep-start').click()
        self.assertTrue(self.page.locator('.step.current').is_visible())

    def choose_time(self, value='2026-11-13T18:00'):
        self.page.locator('.when-input').fill(value)
        self.page.locator('.later .when-use').click()

    def test_both_openings_put_commitment_before_instructions(self):
        for slug in ['guests', 'underwater']:
            self.open_task(slug)
            self.assertIn('Follow the checklist', self.page.locator('.sub').inner_text())
            self.assertIn('Allow about', self.page.locator('.sub').inner_text())
            self.assertIn('When will you start?', self.page.locator('.fork').inner_text())
            self.assertTrue(self.page.locator('.steps').is_hidden())
            self.assertTrue(self.page.locator('.frame').is_hidden())
            self.assertLess(self.page.locator('.go-later').bounding_box()['y'], 844)
            self.start_checklist()
            for _ in range(6):
                self.page.locator('.nav .next').click()
            self.assertTrue(self.page.locator('.done .complete').is_visible())
            self.assertLessEqual(self.page.evaluate('document.documentElement.scrollWidth'), 390)

    def test_one_picker_accepts_tomorrow_and_short_notice(self):
        for query in ['', '?when=tonight&visitday=2026-11-01&arrival=2026-11-01T19:00']:
            self.open_task(query=query)
            self.page.locator('.go-later').click()
            self.assertEqual(self.page.locator('input[type="datetime-local"]').count(), 1)
            self.assertEqual(self.page.locator('.arrival-input').count(), 0)
            self.assertEqual(self.page.locator('.when-picks button').count(), 0)
            for value in ['2026-11-12T17:05', '2026-11-13T18:00']:
                self.choose_time(value)
                self.assertTrue(self.page.locator('.decided').is_visible())
                self.assertIn('Save your start time', self.page.locator('.decided').inner_text())

    def test_invalid_times_and_edits_hide_old_calendar_links(self):
        self.open_task()
        self.page.locator('.go-later').click()
        for value in ['', '2026-11-12T16:00']:
            self.choose_time(value)
            self.assertTrue(self.page.locator('.decided').is_hidden())
            self.assertIn('future day and time', self.page.locator('.schedule-error').inner_text())
        self.choose_time()
        self.page.locator('.when-input').fill('2026-11-14T18:00')
        self.assertTrue(self.page.locator('.decided').is_hidden())

    def test_calendar_roundtrip_and_mid_task_resume(self):
        self.open_task(query='?from=ig-company-tonight&look=career-teal&when=tonight')
        self.page.locator('.go-later').click()
        self.choose_time()
        def invite():
            return unquote(self.page.locator('.cal-ics').get_attribute('href')).replace('\r\n ', '')
        ics = invite()
        self.assertIn('DTSTART:20261114T010000Z', ics)
        self.assertIn('DTEND:20261114T020000Z', ics)
        url = next(line[4:] for line in ics.splitlines() if line.startswith('URL:'))
        q = parse_qs(urlsplit(url).query)
        self.assertEqual(q['resume'], ['1'])
        self.assertEqual(q['from'], ['ig-company-tonight'])
        self.assertEqual(q['look'], ['career-teal'])
        self.assertNotIn('arrival', q)
        self.assertNotIn('visitday', q)
        self.assertNotIn('when', q)
        google = parse_qs(urlsplit(self.page.locator('.cal-google').get_attribute('href')).query)
        self.assertEqual(google['dates'], ['20261114T010000Z/20261114T020000Z'])
        self.assertIn(url, google['details'][0])
        self.page.goto(url)
        self.page.locator('.resume-start').click()
        self.page.locator('.prep-start').click()
        self.page.locator('.nav .next').click()
        self.page.locator('.nav .bail').click()
        self.choose_time()
        ics = invite()
        self.assertIn('step=2', ics)
        url = next(line[4:] for line in ics.splitlines() if line.startswith('URL:'))
        self.page.goto(url)
        self.page.locator('.resume-start').click()
        self.page.locator('.prep-start').click()
        self.assertIn('Empty the sink', self.page.locator('.step.current h2').inner_text())

    def test_preparation_can_return_to_scheduling(self):
        self.open_task('underwater')
        self.page.locator('.go-do').click()
        self.page.locator('.prep-cancel').click()
        self.assertTrue(self.page.locator('.later').is_visible())
        self.assertTrue(self.page.locator('.frame').is_hidden())

    def test_other_tasks_and_print_remain_available(self):
        self.open_task('dinner')
        self.assertTrue(self.page.locator('.frame').is_visible())
        self.page.locator('.go-do').click()
        self.assertTrue(self.page.locator('.step.current').is_visible())
        self.page.locator('.nav .bail').click()
        self.assertGreater(self.page.locator('.when-picks button').count(), 0)
        import re
        for slug in ['guests', 'underwater']:
            self.open_task(slug)
            self.page.evaluate('document.fonts.ready')
            pdf = self.page.pdf(format='Letter', print_background=True)
            self.assertEqual(len(re.findall(rb'/Type /Page\b', pdf)), 1)

if __name__ == '__main__':
    unittest.main()
