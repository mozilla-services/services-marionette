from firefox_puppeteer.ui.browser.notifications import (
    AddOnInstallBlockedNotification,
    AddOnInstallConfirmationNotification,
    AddOnInstallCompleteNotification)
from marionette_driver import By


def test_install(base_url, firefox, marionette):
    marionette.navigate('{0}/en-US/firefox/addon/memchaser/'.format(base_url))
    marionette.find_element(
        By.CSS_SELECTOR,
        '#addon .install-button a').click()
    with marionette.using_context(marionette.CONTEXT_CHROME):
        if 'allizom' in base_url:
            firefox.wait_for_notification(AddOnInstallBlockedNotification)
            firefox.notification.allow()
        firefox.wait_for_notification(AddOnInstallConfirmationNotification)
        firefox.notification.install()
        firefox.wait_for_notification(AddOnInstallCompleteNotification)
        firefox.notification.close()
