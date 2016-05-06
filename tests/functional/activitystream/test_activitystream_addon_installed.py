# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from apps.activitystream.app import ActivityStream


class TestActivityStreamAddonInstalled(object):

    def test_activitystream_addon_installed(self, install_xpi, puppeteer):
        activity_stream = ActivityStream(puppeteer)
