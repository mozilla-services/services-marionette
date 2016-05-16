# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


from marionette_driver import By


from apps.base import Base, PageRegion


class Pocket(Base):
    _login_url = 'https://www.getpocket.com/login'
    _pocket_chrome_button = (By.ID, "#pocket-button")
    _login_with_firefox_button_locator = (
        By.CSS_SELECTOR, 'a.btn.login-btn-firefox')
    _pocket_start_saving_button_locator = (
        By.XPATH, '//a[text()="Start Saving"]')
    _pocket_logo_header_locator = (By.CSS_SELECTOR, 'h1.pocket_logo')
    _pocket_username_nav_locator = (By.CSS_SELECTOR, 'span.nav-username')
    _pocket_all_pocket_items_locator = (By.CSS_SELECTOR, '#queue li.item')

    def __init__(self, marionette):
        super(Pocket, self).__init__(marionette)
        self.wait_for_element_displayed(*self._pocket_logo_header_locator)
        self.wait_for_element_displayed(*self._pocket_all_pocket_items_locator)

    def click_pocket_chrome_button(self):
        with self.marionette.using_context(self.CHROME):
            self.wait_for_element_displayed(
                *self._pocket_chrome_button).click()

    @property
    def username(self):
        return self.get_element_text(*self._pocket_username_nav_locator)

    @property
    def queue_items(self):
        return [self.QueueItem(self.marionette, queue_item) for queue_item in
                self.marionette.find_elements(*self._pocket_all_pocket_items_locator)]

    class QueueItem(PageRegion):
        # TODO: Create methods for all of these different properties and
        # functions.

        @property
        def header(self):
            pass

        @property
        def body(self):
            pass

        @property
        def url(self):
            pass

        @property
        def tags(self):
            pass

        def toggle_favorite(self):
            pass

        def delete(self):
            pass

        def archive(self):
            pass

        def add_tag(self):
            pass

        def delete_tag(self):
            pass
