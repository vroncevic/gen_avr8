# -*- coding: UTF-8 -*-

'''
Module
    factory_test.py
Info
    Unit tests for GenAVR8BundleFactory class.
'''

from __future__ import annotations

import unittest

from gen_avr8.setup.bundle import GenAVR8Bundle
from gen_avr8.setup.factory import GenAVR8BundleFactory


class TestGenAVR8BundleFactory(unittest.TestCase):

    def test_create_bundle_default(self) -> None:
        bundle = GenAVR8BundleFactory.create_bundle()
        self.assertIsInstance(bundle, GenAVR8Bundle)

    def test_create_bundle_with_options(self) -> None:
        options = {'info_file': 'gen_avr8/infrastructure/config/gen_avr8.cfg'}
        bundle = GenAVR8BundleFactory.create_bundle(options)
        self.assertIsInstance(bundle, GenAVR8Bundle)

    def test_create_bundle_invalid_options(self) -> None:
        options = {'info_file': 123}
        with self.assertRaises(Exception):
            GenAVR8BundleFactory.create_bundle(options)

    def test_get_version(self) -> None:
        self.assertEqual(GenAVR8BundleFactory.get_version(), '2.6.6')
