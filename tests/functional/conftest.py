# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from firefox_puppeteer import Puppeteer
from firefox_puppeteer.ui.browser.window import BrowserWindow  # noqa

from marionette_driver.marionette import Marionette

TIMEOUT = 20


def pytest_addoption(parser):
    parser.addoption(
        '--bin',
        default='/Applications/FirefoxNightly.app/Contents/MacOS/firefox-bin',
        help='path for Firefox binary')
    parser.addoption(
        '--base-url',
        metavar='url',
        help='base url for the application under test.'
    )
    parser.addoption(
        '--addon-path',
        metavar='addon path',
        help='path to addon to be installed before test'
    )


@pytest.fixture
def marionette(request, timeout):
    """Return a marionette instance"""
    m = Marionette(bin=request.config.option.bin)
    m.start_session()
    m.set_prefs({'signon.rememberSignons': False})
    request.addfinalizer(m.delete_session)
    m.set_search_timeout(timeout)
    return m


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
def firefox(puppeteer):
    firefox = puppeteer.windows.current
    with puppeteer.marionette.using_context(
            puppeteer.marionette.CONTEXT_CHROME):
                firefox.focus()
    puppeteer.marionette.set_context(puppeteer.marionette.CONTEXT_CONTENT)
    return firefox


@pytest.fixture
def timeout():
    """Return default timeout"""
    return TIMEOUT


@pytest.fixture
def install_addons(marionette, request):
    from marionette_driver.addons import Addons
    addons = Addons(marionette)
    addons.install(request.config.option.addon)
    marionette.restart()
