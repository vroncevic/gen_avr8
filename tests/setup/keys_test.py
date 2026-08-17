# -*- coding: UTF-8 -*-

'''
Module
    keys_test.py
Info
    Unit tests for GenAVR8BundleKeys class.
'''

from __future__ import annotations

import unittest
from types import MappingProxyType

from gen_avr8.setup.keys import GenAVR8BundleKeys


class TestGenAVR8BundleKeys(unittest.TestCase):

    def test_get_dependency_to_type(self) -> None:
        deps = GenAVR8BundleKeys.get_dependency_to_type()
        self.assertIsInstance(deps, MappingProxyType)
        self.assertIn(GenAVR8BundleKeys.DEPENDENCY_BASE, deps)
        self.assertIn(GenAVR8BundleKeys.DEPENDENCY_SERVICE, deps)
        self.assertIn(GenAVR8BundleKeys.DEPENDENCY_SUBPROCESSOR, deps)
        self.assertIn(GenAVR8BundleKeys.DEPENDENCY_CLI, deps)

    def test_get_option_to_type(self) -> None:
        opts = GenAVR8BundleKeys.get_option_to_type()
        self.assertIsInstance(opts, MappingProxyType)
        self.assertIn(GenAVR8BundleKeys.OPTION_INFO_FILE, opts)
