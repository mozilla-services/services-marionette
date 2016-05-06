# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from firefox_puppeteer import Puppeteer
from firefox_puppeteer.ui.browser.window import BrowserWindow
from marionette_driver.marionette import Marionette
import pytest


def pytest_addoption(parser):
    pass
    # parser.addoption(
    #     '--base-url',
    #     default='https://addons-dev.allizom.org',
    #     help='base url for the application under test.')
    # parser.addoption(
    #     '--firefox-path',
    #     default='/usr/local/bin/firefox',
    #     help='path for Firefox binary')


@pytest.fixture(scope='session')
def base_url(request):
    """Return a base URL"""
    return request.config.getoption('base_url') or 'https://addons-dev.allizom.org'


@pytest.fixture
def marionette(request):
    marionette = Marionette(bin=request.config.getoption('bin'))
    marionette.start_session()
    request.addfinalizer(marionette.delete_session)
    return marionette


@pytest.fixture
def puppeteer(marionette):
    puppeteer = Puppeteer()
    puppeteer.marionette = marionette
    # enable browser toolbox
    puppeteer.prefs.set_pref('devtools.chrome.enabled', True)
    puppeteer.prefs.set_pref('devtools.debugger.remote-enabled', True)
    # prevent ui popups auto-hiding
    puppeteer.prefs.set_pref('ui.popup.disable_autohide', True)
    return puppeteer


@pytest.fixture
def firefox(marionette, puppeteer):
    firefox = puppeteer.windows.current
    with marionette.using_context(marionette.CONTEXT_CHROME):
        firefox.focus()
    marionette.set_context(marionette.CONTEXT_CONTENT)
    return firefox
