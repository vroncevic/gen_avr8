# -*- coding: UTF-8 -*-

'''
Module
    osc_selector_test.py
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
    Defines class OSCSelectorTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of OSCSelector.
Execute
    python3 -m unittest -v osc_selector_test
'''

import sys
from typing import List
from unittest.mock import patch
from unittest import TestCase, main

try:
    from gen_avr8.pro.osc_selector import OSCSelector
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


class OSCSelectorTestCase(TestCase):
    '''
        Defined class OSCSelectorTestCase with attribute(s) and method(s).
        Created test cases for checking functionalities of OSCSelector.
        OSCSelector unittests.

        It defines:

            :attributes:
                | osc_select - OSCSelector object.
                | osc_target - Selected OSC target.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_selected_osc - Test choose OSC target.
                | test_is_target_str_type - Test is target str type.
                | test_checks_osc - Test checks selected OSC name.
    '''

    def setUp(self) -> None:
        '''Call before test case'''
        self.osc_select = OSCSelector()
        self.osc_target = '-1234567890'

    def tearDown(self) -> None:
        '''Call after test case'''
        self.osc_select = None
        self.osc_target = None

    def test_selected_osc(self) -> None:
        '''Test for selected OSC'''
        with patch('builtins.input', return_value='9') as select:
            if select:
                if self.osc_select:
                    self.assertEqual(
                        self.osc_select.choose_osc(), '16000000UL'
                    )
                    select.assert_called_once_with(' select FOSC: ')

    def test_is_target_str_type(self) -> None:
        '''Test is target str type.'''
        self.assertTrue(isinstance(self.osc_target, str))

    def test_checks_osc(self) -> None:
        '''Test checks selected OSC name.'''
        if self.osc_select:
            osc_list: List[str] | None = self.osc_select.get_fosc_list()
            if osc_list:
                self.assertFalse(self.osc_target in osc_list)


if __name__ == '__main__':
    main()
