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

    def open_tonight(self, extra=''):
        self.page.goto(self.origin + '/guests.html?when=tonight&from=ig-company-tonight&look=career-teal' + extra)
        self.page.locator('.go-later').click()

    def select_times(self, start='2026-11-12T18:00', arrival='2026-11-12T19:30'):
        self.page.locator('.arrival-input').fill(arrival)
        self.page.locator('.prep-input').fill(start)
        self.page.locator('.when-use').click()

    def test_tonight_links_return_to_task_and_current_step(self):
        self.open_tonight()
        self.assertEqual(self.page.locator('.when-picks button').count(), 0)
        self.assertIn('tonight', self.page.locator('h1').inner_text())
        self.select_times()
        self.assertTrue(self.page.locator('.decided').is_visible())
        ics = unquote(self.page.locator('.cal-ics').get_attribute('href')).replace('\r\n ', '')
        self.assertIn('DTSTART:20261113T010000Z', ics)
        self.assertIn('DTEND:20261113T020000Z', ics)
        url = next(line[4:] for line in ics.splitlines() if line.startswith('URL:'))
        q = parse_qs(urlsplit(url).query)
        for key, value in {'resume':'1','when':'tonight','visitday':'2026-11-12','arrival':'2026-11-12T19:30','from':'ig-company-tonight','look':'career-teal'}.items():
            self.assertEqual(q[key], [value])
        google = parse_qs(urlsplit(self.page.locator('.cal-google').get_attribute('href')).query)
        self.assertEqual(google['dates'], ['20261113T010000Z/20261113T020000Z'])
        self.assertIn(url, google['details'][0])
        self.page.goto(url)
        self.page.locator('.resume-start').click()
        self.assertIn('Bag the kitchen trash', self.page.locator('.step.current h2').inner_text())
        self.page.locator('.nav .next').click()
        self.page.locator('.nav .bail').click()
        self.select_times()
        ics = unquote(self.page.locator('.cal-ics').get_attribute('href')).replace('\r\n ', '')
        self.assertIn('step=2', ics)

    def test_rejects_past_tomorrow_and_insufficient_lead_time(self):
        self.open_tonight()
        for start, arrival, message in [
            ('2026-11-13T18:00','2026-11-13T20:00','arrival'),
            ('2026-11-12T16:00','2026-11-12T20:00','future time'),
            ('2026-11-12T19:00','2026-11-12T19:30','at least an hour'),
            ('2026-11-12T20:00','2026-11-12T19:30','at least an hour')]:
            self.select_times(start, arrival)
            self.assertTrue(self.page.locator('.decided').is_hidden())
            self.assertIn(message, self.page.locator('.schedule-error').inner_text())

    def test_changes_invalidate_old_calendar_links(self):
        self.open_tonight()
        self.select_times()
        self.page.locator('.arrival-input').fill('2026-11-12T18:15')
        self.assertTrue(self.page.locator('.decided').is_hidden())

    def test_expired_return_does_not_claim_tonight(self):
        for suffix in ['&resume=1&visitday=2026-11-11&arrival=2026-11-11T20:00',
                       '&resume=1&visitday=2026-11-12&arrival=2026-11-12T16:00']:
            self.page.goto(self.origin + '/guests.html?when=tonight' + suffix)
            self.assertNotIn('tonight', self.page.locator('h1').inner_text())
            self.assertTrue(self.page.locator('.go-later').is_hidden())
            self.assertEqual(self.page.locator('.resume-move').count(), 0)
            self.assertNotIn('This is the time you picked', self.page.locator('.resume').inner_text())
            self.assertTrue(self.page.get_by_role('link', name='Plan another visit').is_visible())
            self.page.get_by_role('link', name='Plan another visit').click()
            self.assertNotIn('when=', self.page.url)

    def test_midnight_blocks_reusing_open_form(self):
        self.open_tonight()
        self.select_times()
        self.page.clock.set_fixed_time(datetime.fromisoformat('2026-11-13T07:01:00+00:00'))
        self.page.locator('.when-use').click()
        self.assertIn('visit date has passed', self.page.locator('.schedule-error').inner_text())
        self.assertTrue(self.page.locator('.decided').is_hidden())

    def test_generic_company_and_reset_keep_full_execution(self):
        for slug, heading, cta in [('guests','Someone\'s coming over.', 'Start getting ready'), ('underwater','The dishes are piled up.', 'Start the reset')]:
            self.page.goto(self.origin + '/' + slug + '.html')
            self.assertIn(heading, self.page.locator('h1').inner_text())
            self.assertIn(cta, self.page.locator('.go-do').inner_text())
            self.assertEqual(self.page.locator('.step').count(), 6)
            self.page.locator('.go-later').click()
            self.assertGreater(self.page.locator('.when-picks button').count(), 0)
            self.page.locator('.when-picks button').first.click()
            self.assertTrue(self.page.locator('.cal-ics').is_visible())
            self.page.locator('.go-do').click()
            for _ in range(6):
                self.page.locator('.nav .next').click()
            self.assertTrue(self.page.locator('.done .complete').is_visible())
            self.assertLessEqual(self.page.evaluate('document.documentElement.scrollWidth'), 390)

if __name__ == '__main__':
    unittest.main()
