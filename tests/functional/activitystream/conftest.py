# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os
import pytest

from fxapom.fxapom import FxATestAccount, WebDriverFxA, PROD_URL

from marionette_driver import By, expected,  Wait


@pytest.fixture(scope='function')
def install_xpi(marionette, timeout):
    from marionette_driver.addons import Addons
    from urllib import URLopener
    activity_stream_xpi = URLopener()

    xpi_path = os.path.dirname(os.getcwd())
    xpi_file_path = os.path.join(xpi_path, 'activity_stream.xpi')
    activity_stream_xpi.retrieve('https://moz-activity-streams-dev.s3.amazonaws.com/dist/activity-streams-latest.xpi',
                                 xpi_file_path)
    addons = Addons(marionette)
    print xpi_file_path
    addons.install(xpi_file_path)


@pytest.fixture(scope='function')
def add_browsing_history(marionette, timeout):
    _reddit_post_list = (By.ID, 'siteTable')

    marionette.navigate('https://www.reddit.com/r/mozilla/')
    Wait(marionette, timeout).until(
        expected.element_displayed(Wait(marionette, timeout).until(
            expected.element_present(*_reddit_post_list))
        )
    )
    marionette.navigate('https://www.reddit.com/r/firefox/')
    Wait(marionette, timeout).until(
        expected.element_displayed(Wait(marionette, timeout).until(
            expected.element_present(*_reddit_post_list))
        )
    )
    marionette.navigate('https://www.reddit.com/r/yahoo/')
    Wait(marionette, timeout).until(
        expected.element_displayed(Wait(marionette, timeout).until(
            expected.element_present(*_reddit_post_list))
        )
    )
