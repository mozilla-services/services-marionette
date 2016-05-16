# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest


from fxapom.fxapom import FxATestAccount, WebDriverFxA, DEV_URL

from marionette_driver import By, Wait, expected


@pytest.fixture(scope='session')
def base_url(request):
    """Return a base URL"""
    return request.config.getoption(
        'base_url') or 'http://testpilot.dev.mozaws.net/?butimspecial'


@pytest.fixture
def fxa_account():
    """Return a new fxa account"""
    return FxATestAccount(DEV_URL)


@pytest.fixture
def user(fxa_account):
    """Return user credentials"""
    # return {
    #     'email': 'jdorlus@mozilla.com',
    #     'password': 'password',
    #     'name': fxa_account.email.split('@')[0]
    # }
    return {
        'email': fxa_account.email,
        'password': fxa_account.password,
        'name': fxa_account.email.split('@')[0]
    }


@pytest.fixture(scope='function')
def sign_in(base_url, marionette, user, timeout):
    """Handle logging into fxa"""
    _testpilot_sign_get_started_fxa_button_locator = (
        By.XPATH, '//button[text()="Sign in"]')
    _fxa_login_link_locator = (
        By.CSS_SELECTOR, 'div.links a.sign-in')

    marionette.navigate('%s/' % base_url)
    Wait(marionette, timeout).until(
        expected.element_displayed(
            *_testpilot_sign_get_started_fxa_button_locator)
    )
    marionette.find_element(
        *_testpilot_sign_get_started_fxa_button_locator).click()
    Wait(marionette, timeout).until(
        expected.element_displayed(
            Wait(marionette, timeout).until(
                expected.element_present(*_fxa_login_link_locator)))
    )
    marionette.find_element(*_fxa_login_link_locator).click()
    driver = WebDriverFxA(marionette, timeout)
    driver.sign_in(user['email'], user['password'])
