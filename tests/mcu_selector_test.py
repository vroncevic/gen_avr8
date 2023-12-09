# -*- coding: UTF-8 -*-

'''
Module
    mcu_selector_test.py
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
    python3 -m unittest -v mcu_selector_test
'''

import sys
import io
from typing import List, Any
from unittest.mock import patch
from unittest import TestCase, main

try:
    from gen_avr8.pro.mcu_selector import MCUSelector
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2022, https://vroncevic.github.io/gen_avr8'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_avr8/blob/dev/LICENSE'
__version__ = '2.5.5'
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

    @patch('builtins.input', return_value='37')
    def test_selected_atmega8(self, mock_input: Any) -> None:
        '''Test chooses MCU atmega8 target'''
        mcu_select: MCUSelector | None = MCUSelector()
        if mcu_select:
            self.assertEqual(mcu_select.choose_mcu(), 'atmega8')
            mock_input.assert_called_once_with(' select MCU: ')

    @patch('builtins.input', return_value='42')
    def test_selected_attiny24(self, mock_input: Any) -> None:
        '''Test chooses MCU attiny24 target'''
        mcu_select: MCUSelector | None = MCUSelector()
        if mcu_select:
            called_mcu: Any = mock_input()
            self.assertTrue(called_mcu == '42')
            self.assertEqual(mcu_select.choose_mcu(), 'attiny24')

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['137', '37'])
    def test_selected_unknown(self, mock_input: Any, mock_output: Any) -> None:
        '''Test chooses unknown MCU target'''
        mcu_select: MCUSelector | None = MCUSelector()
        if mcu_select and mock_input and mock_output:
            mcu_select.choose_mcu()
            content = str(mock_output.getvalue())
            self.assertTrue("not an appropriate choice" in content)

    def test_checks_mcu(self) -> None:
        '''Test checks selected MCU name'''
        mcu_select: MCUSelector | None = MCUSelector()
        mcu_target: str | None = 'atmega8'
        if mcu_select:
            mcu_list: List[str] | None = mcu_select.get_mcu_list()
            if mcu_list:
                self.assertTrue(mcu_target in mcu_list)


if __name__ == '__main__':
    main()
