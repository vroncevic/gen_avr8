# -*- coding: UTF-8 -*-

'''
Module
    avr8_setup_test.py
Copyright
    Copyright (C) 2018 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines class AVR8SetupTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of AVR8Setup.
Execute
    python3 -m unittest -v avr8_setup_test
'''

import sys
from typing import Any, List, Optional
from unittest import TestCase, main
from unittest.mock import patch

try:
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from gen_avr8.pro import AVR8Setup
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/gen_avr8'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/gen_avr8/blob/dev/LICENSE'
__version__: str = '2.6.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class AVR8SetupTestCase(TestCase):
    '''
        Defines class AVR8SetupTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of AVR8Setup.
        AVR8Setup unit tests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_create - Test create (not None).
                | test_pro_setup - Test project setup.
                | test_pro_setup_name_none - Test pro setup None name.
                | test_pro_setup_type_none - Test pro setup None type.
                | test_pro_gen_setup_without_params - Test no params.
                | test_pro_gen_setup_with_empty_params - Test empty params.
                | test_pro_gen_setup_with_params - Test with with params.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_create(self) -> None:
        '''Test create (not None)'''
        avr_setup: Optional[AVR8Setup] = AVR8Setup()
        self.assertIsNotNone(avr_setup)

    def test_pro_setup(self) -> None:
        '''Test project setup'''
        avr_setup: Optional[AVR8Setup] = AVR8Setup()
        if avr_setup:
            self.assertIsInstance(avr_setup, AVR8Setup)
            avr_setup.project_setup('new_simple_test', 'app')

    def test_pro_setup_name_none(self) -> None:
        '''Test pro setup None name'''
        avr_setup: Optional[AVR8Setup] = AVR8Setup()
        if avr_setup:
            with self.assertRaises(ATSTypeError):
                self.assertIsInstance(avr_setup, AVR8Setup)
                avr_setup.project_setup(None, 'app')

    def test_pro_setup_type_none(self) -> None:
        '''Test pro setup None type'''
        avr_setup: Optional[AVR8Setup] = AVR8Setup()
        if avr_setup:
            with self.assertRaises(ATSTypeError):
                self.assertIsInstance(avr_setup, AVR8Setup)
                avr_setup.project_setup('new_simple_test', None)

    @patch('builtins.input', side_effect=['37', '9'])
    def test_pro_gen_setup_without_params(self, mock_input: Any) -> None:
        '''Test no params'''
        avr_setup: Optional[AVR8Setup] = AVR8Setup()
        if avr_setup and mock_input:
            self.assertFalse(avr_setup.gen_pro_setup())

    @patch('builtins.input', side_effect=['37', '9'])
    def test_pro_gen_setup_with_empty_params(self, mock_input: Any) -> None:
        '''Test empty params'''
        avr_setup: Optional[AVR8Setup] = AVR8Setup()
        if avr_setup and mock_input:
            avr_setup.project_setup('', '')
            self.assertFalse(avr_setup.gen_pro_setup())

    @patch('builtins.input', side_effect=['37', '9'])
    def test_pro_gen_setup_with_params(self, mock_input: Any) -> None:
        '''Test with with params'''
        avr_setup: Optional[AVR8Setup] = AVR8Setup()
        if avr_setup and mock_input:
            avr_setup.project_setup('new_simple_test', 'app')
            self.assertTrue(avr_setup.gen_pro_setup())


if __name__ == '__main__':
    main()
