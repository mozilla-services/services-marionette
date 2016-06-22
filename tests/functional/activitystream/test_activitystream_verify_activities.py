# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from apps.activitystream.app import ActivityStream


class TestActivityStreamVerifyActivities(object):

    def test_activitystream_verify_activities(
            self, install_xpi, add_browsing_history, puppeteer):
        activity_stream = ActivityStream(puppeteer)  # noqa
