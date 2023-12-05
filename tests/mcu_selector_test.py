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
from unittest.mock import patch
from unittest import TestCase, main
from typing import List

try:
    from gen_avr8.pro.mcu_selector import MCUSelector
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
                | mcu_select - MCUSelector object.
                | mcu_target - Selected MCU target.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_selected_atmega8 - Test chooses MCU atmega8 target.
                | test_target_mcu_is_str - Test checks type of target.
                | test_checks_mcu - Test checks selected MCU name.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.mcu_select = MCUSelector()
        self.mcu_target = 'atmega-1'

    def tearDown(self) -> None:
        '''Call after test case.'''
        self.mcu_select = None
        self.mcu_target = None

    def test_selected_atmega8(self) -> None:
        '''Test chooses MCU atmega8 target'''
        with patch('builtins.input', return_value='37') as select:
            if select:
                if self.mcu_select:
                    self.assertEqual(self.mcu_select.choose_mcu(), 'atmega8')
                    select.assert_called_once_with(' select MCU: ')

    def test_target_mcu_is_str(self) -> None:
        '''Test checks type of target'''
        self.assertEqual(isinstance(self.mcu_target, str), True)

    def test_checks_mcu(self) -> None:
        '''Test checks selected MCU name'''
        if self.mcu_select:
            mcu_list: List[str] | None = self.mcu_select.get_mcu_list()
            if mcu_list:
                self.assertFalse(self.mcu_target in mcu_list)


if __name__ == '__main__':
    main()
