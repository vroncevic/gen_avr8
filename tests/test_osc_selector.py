# -*- coding: UTF-8 -*-

'''
 Module
     test_osc_selector.py
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
     Defined class OSCSelectorTestCase with attribute(s) and method(s).
     Created test cases for checking functionalities of OSCSelector.
 Execute
     python3 -m unittest -v test_osc_selector
'''

import sys
import unittest

try:
    from mock import patch
    from gen_avr8.pro.osc_selector import OSCSelector
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


class OSCSelectorTestCase(unittest.TestCase):
    '''
        Defined class OSCSelectorTestCase with attribute(s) and method(s).
        Created test cases for checking functionalities of OSCSelector.
        It defines:

            :attributes:
                | osc_select - OSCSelector object.
                | osc_target - Selected OSC target.
            :methods:
                | setUp - call before test case.
                | tearDown - call after test case.
                | test_choose_osc - Test choose OSC target.
                | test_check_osc - Test check selected OSC name.
    '''

    def setUp(self):
        '''Call before test case.'''
        self.osc_select = OSCSelector()
        self.osc_target = '-1234567890'

    def tearDown(self):
        '''Call after test case.'''
        self.osc_select = None
        self.osc_target = None

    def test_16000000UL(self):
        with patch('builtins.input', return_value='9') as _input:
            self.assertEqual(self.osc_select.choose_osc(), '16000000UL')
            _input.assert_called_once_with(' select FOSC: ')

    def test_choose_osc(self):
        '''Test choose OSC target.'''
        self.assertEqual(isinstance(self.osc_target, str), True)

    def test_check_osc(self):
        '''Test check selected OSC name.'''
        self.assertEqual(
            self.osc_target in self.osc_select.get_fosc_list(), False
        )


if __name__ == '__main__':
    unittest.main()
