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
from argparse import Namespace

try:
    from gen_avr8 import GenAVR8
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
                | test_create - Test chooses MCU atmega8 target.
                | test_process - Test chooses MCU attiny24 target.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_create(self) -> None:
        '''Test create'''
        avr_gen: GenAVR8 | None = GenAVR8()
        self.assertIsNotNone(avr_gen)

    @patch(
        'argparse.ArgumentParser.parse_args',
        return_value=Namespace(
            gen='tester', type='app', verbose=False
        )
    )
    @patch('builtins.input', return_value='9')
    def test_process(self, mock_input: Any, mock_parse: Any) -> None:
        '''Test create'''
        avr_gen: GenAVR8 | None = GenAVR8()
        if avr_gen and mock_input and mock_parse:
            self.assertIsInstance(avr_gen, GenAVR8)
            self.assertTrue(avr_gen.process())


if __name__ == '__main__':
    main()
