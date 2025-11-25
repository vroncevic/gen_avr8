# -*- coding: UTF-8 -*-

'''
Module
    osc_selector_test.py
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
    Defines class OSCSelectorTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of OSCSelector.
Execute
    python3 -m unittest -v osc_selector_test
'''

import sys
import io
from typing import Any, List, Optional
from unittest.mock import patch
from unittest import TestCase, main

try:
    from gen_avr8.pro.osc_selector import OSCSelector
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


class OSCSelectorTestCase(TestCase):
    '''
        Defines class OSCSelectorTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of OSCSelector.
        OSCSelector unit tests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_selected_osc - Test choose OSC target.
                | test_selected_unknown - Test chooses unknown OSC target.
                | test_checks_osc - Test checks selected OSC name.
    '''

    def setUp(self) -> None:
        '''Call before test case'''

    def tearDown(self) -> None:
        '''Call after test case'''

    @patch('builtins.input', return_value='9')
    def test_selected_osc(self, mock_input: Any) -> None:
        '''Test choose OSC target'''
        osc_select: Optional[OSCSelector] = OSCSelector()
        if osc_select:
            self.assertEqual(osc_select.choose_osc(), '16000000UL')
            mock_input.assert_called_once_with(' select FOSC: ')

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['137', '9'])
    def test_selected_unknown(self, mock_input: Any, mock_output: Any) -> None:
        '''Test chooses unknown OSC target'''
        osc_select: Optional[OSCSelector] = OSCSelector()
        if osc_select and mock_input and mock_output:
            osc_select.choose_osc()
            content = str(mock_output.getvalue())
            self.assertTrue("not an option" in content)

    def test_checks_osc(self) -> None:
        '''Test checks selected OSC name.'''
        osc_select: Optional[OSCSelector] = OSCSelector()
        if osc_select:
            osc_list: List[str] | None = osc_select.get_fosc_list()
            if osc_list:
                self.assertTrue('16000000UL' in osc_list)


if __name__ == '__main__':
    main()
