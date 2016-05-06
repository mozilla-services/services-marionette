# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from fxapom.fxapom import FxATestAccount, WebDriverFxA, PROD_URL

from marionette_driver import By, expected,  Wait


@pytest.fixture(scope='session')
def base_url(request):
    """Return a base URL"""
    return request.config.getoption('base_url') or 'https://www.getpocket.com/login'

@pytest.fixture
def fxa_account():
    """Return a new fxa account"""
    return FxATestAccount(PROD_URL)


@pytest.fixture
def user(fxa_account):
    """Return user credentials"""
    return {
        'email': fxa_account.email,
        'password': fxa_account.password,
        'name': fxa_account.email.split('@')[0]
    }


@pytest.fixture(scope='function')
def sign_in(base_url, marionette, user, timeout):
    """Handle logging into fxa"""
    _pocket_log_in_firefox_locator = (
        By.CSS_SELECTOR, '.login-btn-firefox')
    _pocket_accept_permission_locator = (
        By.CSS_SELECTOR, '#accept'
    )
    _pocket_email_address_accept_locator = (
        By.CSS_SELECTOR, 'div.fxa-checkbox__value'
    )
    marionette.navigate('%s/' % base_url)
    Wait(marionette, timeout).until(
        expected.element_displayed(Wait(marionette, timeout).until(
            expected.element_present(*_pocket_log_in_firefox_locator))
        )
    )
    marionette.find_element(*_pocket_log_in_firefox_locator).click()
    driver = WebDriverFxA(marionette, timeout)
    driver.sign_in(user['email'], user['password'])
    Wait(marionette, timeout).until(
        expected.element_displayed(Wait(marionette,timeout).until(
            expected.element_present(*_pocket_accept_permission_locator))
        )
    )
    assert marionette.find_element(*_pocket_email_address_accept_locator).text == user['email']
    marionette.find_element(*_pocket_accept_permission_locator).click()
