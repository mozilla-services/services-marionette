# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from apps.base import Base

from firefox_puppeteer.testcases import BaseFirefoxTestCase

from marionette_driver import By


class ActivityStream(Base, BaseFirefoxTestCase):

    _activitystream_top_sites_header = (By.XPATH, '//h3[text()="Top Sites"]')

    def __init__(self, puppeteer):
        super(ActivityStream, self).__init__(puppeteer.marionette)

        self.set_context(self.CHROME)
        self.browser = self.windows.current

        self.browser.focus()
        self.browser.tabbar.open_tab()
        self.set_context(self.CONTENT)
        self.wait_for_element_displayed(*self._activitystream_top_sites_header)

    @property
    def top_sites(self):
        pass

