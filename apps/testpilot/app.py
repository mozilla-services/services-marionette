# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from marionette_driver import By

from firefox_puppeteer.ui.browser.notifications import (
    AddOnInstallBlockedNotification,
    AddOnInstallConfirmationNotification,
    AddOnInstallCompleteNotification)

from apps.base import Base


class TestPilot(Base):
    _login_with_firefox_button_locator = (
        By.CSS_SELECTOR, 'div.cta-layout a.fxa-alternate')
    _testpilot_install_addon_button_locator = (
        By.CSS_SELECTOR, '[data-l10n-id="landingInstallButton"]')

    def __init__(self, puppeteer, firefox, url):
        super(TestPilot, self).__init__(puppeteer.marionette)
        self.wait_for_element_displayed(
            *self._testpilot_install_addon_button_locator)
        self.click_element(*self._testpilot_install_addon_button_locator)
        with self.marionette.using_context(self.marionette.CONTEXT_CHROME):
            if 'dev' in url:
                firefox.wait_for_notification(AddOnInstallBlockedNotification)
                print self.marionette.find_element(By.ID, 'notification-popup')
                firefox.notification.allow()
            firefox.wait_for_notification(AddOnInstallConfirmationNotification)
            firefox.notification.install()
            firefox.wait_for_notification(AddOnInstallCompleteNotification)
            firefox.notification.close()
