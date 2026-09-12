# -*- coding: UTF-8 -*-

'''
Module
    gen_avr8_command_test.py
Info
    Unit tests for GenAVR8CommandDefinition and GenAVR8CommandExecutor.
'''

from __future__ import annotations

import unittest
from unittest.mock import Mock

from gen_avr8.core.service.iservice import IService
from gen_avr8.infrastructure.command.gen_avr8_command_definition import GenAVR8CommandDefinition
from gen_avr8.infrastructure.command.gen_avr8_command_executor import GenAVR8CommandExecutor


class TestGenAVR8Command(unittest.TestCase):

    def test_definition(self) -> None:
        definition = GenAVR8CommandDefinition()
        self.assertEqual(definition.name, 'create')
        self.assertEqual(definition.help_text, 'Generate AVR8 project files')
        self.assertEqual(len(definition.options), 3)
        self.assertTrue(isinstance(str(definition), str))

    def test_executor_execute_success(self) -> None:
        definition = GenAVR8CommandDefinition()
        executor = GenAVR8CommandExecutor(definition)
        
        mock_service = Mock(spec=IService)
        mock_service.is_initialized.return_value = True
        mock_service.execute.return_value = {'returncode': 0}
        
        params = {'name': 'test', 'output': '.'}
        result = executor.execute(params=params, service=mock_service)
        
        self.assertEqual(result['returncode'], 0)
        mock_service.execute.assert_called_once_with(params=params)

    def test_executor_execute_not_initialized(self) -> None:
        definition = GenAVR8CommandDefinition()
        executor = GenAVR8CommandExecutor(definition)
        
        mock_service = Mock(spec=IService)
        mock_service.is_initialized.return_value = False
        
        result = executor.execute(params={}, service=mock_service)
        self.assertEqual(result['returncode'], 1)
        self.assertIn('service not initialized', result['stderr'])

    def test_executor_str_representation(self) -> None:
        definition = GenAVR8CommandDefinition()
        executor = GenAVR8CommandExecutor(definition)
        self.assertTrue(isinstance(str(executor), str))

    def test_executor_get_definition(self) -> None:
        definition = GenAVR8CommandDefinition()
        executor = GenAVR8CommandExecutor(definition)
        self.assertEqual(executor.get_definition(), definition)
