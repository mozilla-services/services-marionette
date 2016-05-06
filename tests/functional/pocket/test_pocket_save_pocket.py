# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from apps.pocket.app import Pocket


class TestPocketFxASignIn(object):

    def test_sign_into_pocket_with_fxa(self, sign_in, user,  marionette):
        pocket_page = Pocket(marionette)
        assert pocket_page.username == user['email']
        assert len(pocket_page.queue_items) > 2
