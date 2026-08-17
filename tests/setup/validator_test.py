# -*- coding: UTF-8 -*-

'''
Module
    validator_test.py
Info
    Unit tests for GenAVR8BundleValidator class.
'''

from __future__ import annotations

import unittest
from unittest.mock import Mock

from ats_utilities.base.setup.bundle import BaseBundle

from gen_avr8.core.service.iservice import IService
from gen_avr8.core.service.isubprocessor import ISubProcessor
from gen_avr8.infrastructure.cli.icli import ICLI
from gen_avr8.setup.bundle import GenAVR8Bundle
from gen_avr8.setup.validator import GenAVR8BundleValidator


class DummyService:

    def execute(self, *, params: object) -> object:
        return None

    def is_initialized(self) -> bool:
        return True


class DummySubProcessor:

    def run(self, *, params: object) -> dict[str, object]:
        return {}

    def is_initialized(self) -> bool:
        return True


class DummyCLI:

    def run(self) -> dict[str, object]:
        return {}

    def is_initialized(self) -> bool:
        return True


class TestGenAVR8BundleValidator(unittest.TestCase):

    def test_validate_success(self) -> None:
        mock_base = Mock(spec=BaseBundle)
        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI()

        bundle = GenAVR8Bundle(
            base=mock_base,
            service=dummy_service,
            subprocessor=dummy_subprocessor,
            cli=dummy_cli
        )

        GenAVR8BundleValidator.validate(bundle)

    def test_validate_bundle_none(self) -> None:
        with self.assertRaises(Exception):
            GenAVR8BundleValidator.validate(None)

    def test_validate_bundle_invalid_type(self) -> None:
        with self.assertRaises(Exception):
            GenAVR8BundleValidator.validate("invalid_bundle")

    def test_validate_missing_components(self) -> None:
        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI()

        with self.assertRaises(Exception):
            bundle = GenAVR8Bundle(
                base=None,
                service=dummy_service,
                subprocessor=dummy_subprocessor,
                cli=dummy_cli
            )
            GenAVR8BundleValidator.validate(bundle)

    def test_validate_invalid_component_types(self) -> None:
        mock_base = Mock(spec=BaseBundle)
        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI()

        with self.assertRaises(Exception):
            bundle = GenAVR8Bundle(
                base="invalid",
                service=dummy_service,
                subprocessor=dummy_subprocessor,
                cli=dummy_cli
            )
            GenAVR8BundleValidator.validate(bundle)

        with self.assertRaises(Exception):
            bundle = GenAVR8Bundle(
                base=mock_base,
                service="invalid",
                subprocessor=dummy_subprocessor,
                cli=dummy_cli
            )
            GenAVR8BundleValidator.validate(bundle)

        with self.assertRaises(Exception):
            bundle = GenAVR8Bundle(
                base=mock_base,
                service=dummy_service,
                subprocessor="invalid",
                cli=dummy_cli
            )
            GenAVR8BundleValidator.validate(bundle)

        with self.assertRaises(Exception):
            bundle = GenAVR8Bundle(
                base=mock_base,
                service=dummy_service,
                subprocessor=dummy_subprocessor,
                cli="invalid"
            )
            GenAVR8BundleValidator.validate(bundle)

    def test_is_valid_success(self) -> None:
        mock_base = Mock(spec=BaseBundle)
        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI()

        bundle = GenAVR8Bundle(
            base=mock_base,
            service=dummy_service,
            subprocessor=dummy_subprocessor,
            cli=dummy_cli
        )
        self.assertTrue(GenAVR8BundleValidator.is_valid(bundle))

    def test_is_valid_failure(self) -> None:
        self.assertFalse(GenAVR8BundleValidator.is_valid(None))
        self.assertFalse(GenAVR8BundleValidator.is_valid("invalid"))
