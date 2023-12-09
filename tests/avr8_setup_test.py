# -*- coding: UTF-8 -*-

'''
Module
    avr8_setup_test.py
Copyright
    Copyright (C) 2022 Vladimir Roncevic <elektron.ronca@gmail.com>
    gen_avr8 is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    gen_avr8 is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Defines class MCUSelectorTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of MCUSelector.
Execute
    python3 -m unittest -v avr8_setup_test
'''

import sys
from typing import Any
from unittest import TestCase, main
from unittest.mock import patch

try:
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from gen_avr8.pro import AVR8Setup
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2022, https://vroncevic.github.io/gen_avr8'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_avr8/blob/dev/LICENSE'
__version__ = '2.4.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class MCUSelectorTestCase(TestCase):
    '''
        Defines class MCUSelectorTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of MCUSelector.
        MCUSelector unitteests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_selected_atmega8 - Test chooses MCU atmega8 target.
                | test_selected_attiny24 - Test chooses MCU attiny24 target.
                | test_selected_unknown - Test chooses unknown MCU target.
                | test_checks_mcu - Test checks selected MCU name.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_create(self) -> None:
        '''Test create'''
        avr_setup: AVR8Setup | None = AVR8Setup()
        self.assertIsNotNone(avr_setup)

    def test_pro_setup(self) -> None:
        '''Test create'''
        avr_setup: AVR8Setup | None = AVR8Setup()
        if avr_setup:
            self.assertIsInstance(avr_setup, AVR8Setup)
            avr_setup.project_setup('new_simple_test', 'app')

    def test_pro_setup_name_none(self) -> None:
        '''Test create'''
        avr_setup: AVR8Setup | None = AVR8Setup()
        if avr_setup:
            with self.assertRaises(ATSTypeError):
                self.assertIsInstance(avr_setup, AVR8Setup)
                avr_setup.project_setup(None, 'app')

    def test_pro_setup_type_none(self) -> None:
        '''Test create'''
        avr_setup: AVR8Setup | None = AVR8Setup()
        if avr_setup:
            with self.assertRaises(ATSTypeError):
                self.assertIsInstance(avr_setup, AVR8Setup)
                avr_setup.project_setup('new_simple_test', None)

    @patch('builtins.input', side_effect=['37', '9'])
    def test_pro_gen_setup_without_params(self, mock_input: Any) -> None:
        '''Test project generation without params'''
        avr_setup: AVR8Setup | None = AVR8Setup()
        if avr_setup and mock_input:
            self.assertFalse(avr_setup.gen_pro_setup())

    @patch('builtins.input', side_effect=['37', '9'])
    def test_pro_gen_setup_with_empty_params(self, mock_input: Any) -> None:
        '''Test project generation without params'''
        avr_setup: AVR8Setup | None = AVR8Setup()
        if avr_setup and mock_input:
            avr_setup.project_setup('', '')
            self.assertFalse(avr_setup.gen_pro_setup())

    @patch('builtins.input', side_effect=['37', '9'])
    def test_pro_gen_setup_with_params(self, mock_input: Any) -> None:
        '''Test project generation with params'''
        avr_setup: AVR8Setup | None = AVR8Setup()
        if avr_setup and mock_input:
            avr_setup.project_setup('new_simple_test', 'app')
            self.assertTrue(avr_setup.gen_pro_setup())


if __name__ == '__main__':
    main()
