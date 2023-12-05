# -*- coding: UTF-8 -*-

'''
 Module
     test_module_type.py
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
     Defined class ModuleTypeTestCase with attribute(s) and method(s).
     Created test cases for checking functionalities of ModuleType.
 Execute
     python3 -m unittest -v test_module_type
'''

import sys
import unittest

try:
    from gen_avr8.pro.module_type import ModuleType
except ImportError as test_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, test_error_message)
    sys.exit(MESSAGE)  # Force close python test ############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2022, https://vroncevic.github.io/gen_avr8'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_avr8/blob/dev/LICENSE'
__version__ = '2.4.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ModuleTypeTestCase(unittest.TestCase):
    '''
        Defined class ModuleTypeTestCase with attribute(s) and method(s).
        Created test cases for checking functionalities of ModuleType.
        It defines:

            :attributes:
                | app_module - Project app module.
                | build_module - Project build module.
            :methods:
                | setUp - call before test case.
                | tearDown - call after test case.
                | test_pre_process_module - Test pre-process module.
                | test_is_source_module - Test is source module.
                | test_is_build_module - Test is build module.
    '''

    def setUp(self):
        '''Call before test case.'''
        self.app_module = 'simple_test.c'
        self.build_module = 'Makefile'

    def tearDown(self):
        '''Call after test case.'''
        self.app_module = None
        self.build_module = None

    def test_pre_process_module(self):
        '''Test pre-process module.'''
        self.assertEqual(
            ModuleType.pre_process_module('app', 'simple_test', 'c'), 'c'
        )

    def test_is_source_module(self):
        '''Test is source module.'''
        self.assertEqual(ModuleType.is_source_module(self.app_module), True)

    def test_is_build_module(self):
        '''Test is build module.'''
        self.assertEqual(ModuleType.is_build_module(self.build_module), True)


if __name__ == '__main__':
    unittest.main()
