#  Copyright (c) 2005-2020, Enthought, Inc.
#  All rights reserved.
#
#  This software is provided without warranty under the terms of the BSD
#  license included in LICENSE.txt and may be redistributed only
#  under the conditions described in the aforementioned license.  The license
#  is also available online at http://www.enthought.com/licenses/BSD.txt
#
#  Thanks for using Enthought open source!
#

import unittest

from traitsui.testing.tester.default_registry import get_default_registry
from traitsui.testing.tester.registry import TargetRegistry


class TestDefaultRegistry(unittest.TestCase):

    def test_load_default_registries(self):
        registry = get_default_registry()
        self.assertIsInstance(registry, TargetRegistry)