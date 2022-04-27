# -*- coding: UTF-8 -*-

'''
 Module
     test_mcu_selector.py
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
     Defined class MCUSelectorTestCase with attribute(s) and method(s).
     Created test cases for checking functionalities of MCUSelector.
 Execute
     python3 -m unittest -v test_mcu_selector
'''

import sys
import unittest

try:
    from mock import patch
    from gen_avr8.pro.mcu_selector import MCUSelector
except ImportError as test_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, test_error_message)
    sys.exit(MESSAGE)  # Force close python test ############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2022, https://vroncevic.github.io/gen_avr8'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_avr8/blob/dev/LICENSE'
__version__ = '2.4.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class MCUSelectorTestCase(unittest.TestCase):
    '''
        Defined class MCUSelectorTestCase with attribute(s) and method(s).
        Created test cases for checking functionalities of MCUSelector.
        It defines:

            :attributes:
                | mcu_select - MCUSelector object.
                | mcu_target - Selected MCU target.
            :methods:
                | setUp - call before test case.
                | tearDown - call after test case.
                | test_choose_mcu - Test choose MCU target.
                | test_check_mcu - Test check selected MCU name.
    '''

    def setUp(self):
        '''Call before test case.'''
        self.mcu_select = MCUSelector()
        self.mcu_target = 'atmega-1'

    def tearDown(self):
        '''Call after test case.'''
        self.mcu_select = None
        self.mcu_target = None

    def test_atmega8(self):
        with patch('builtins.input', return_value='37') as _input:
            self.assertEqual(self.mcu_select.choose_mcu(), 'atmega8')
            _input.assert_called_once_with(' select MCU: ')

    def test_choose_mcu(self):
        '''Test choose MCU target.'''
        self.assertEqual(isinstance(self.mcu_target, str), True)

    def test_check_mcu(self):
        '''Test check selected MCU name.'''
        self.assertEqual(
            self.mcu_target in self.mcu_select.get_mcu_list(), False
        )


if __name__ == '__main__':
    unittest.main()
