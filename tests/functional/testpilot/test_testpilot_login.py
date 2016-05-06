# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


from marionette_driver import By, Wait, expected

from apps.testpilot.app import TestPilot


class TestTestPilotLogin(object):

    def test_user_can_log_in(self, sign_in, puppeteer, firefox, base_url):
        test_pilot_page = TestPilot(puppeteer, firefox, base_url)

