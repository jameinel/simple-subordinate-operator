# Copyright 2025 John A Meinel <john@arbash-meinel.com>
# See LICENSE file for licensing details.
#
# Learn more about testing at: https://juju.is/docs/sdk/testing

import unittest

from ops import testing

from charm import SimpleSubordinateOperatorCharm


def test_start():
    # Arrange:
    ctx = testing.Context(SimpleSubordinateOperatorCharm)
    # Act:
    state_out = ctx.run(ctx.on.start(), testing.State())
    # Assert:
    assert state_out.unit_status == testing.ActiveStatus()
