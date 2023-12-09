# -*- coding: UTF-8 -*-

'''
Module
    module_type_test.py
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
    Defines class ModuleTypeTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of ModuleType.
Execute
    python3 -m unittest -v module_type_test
'''

import sys
from unittest import TestCase, main

try:
    from gen_avr8.pro.module_type import ModuleType
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


class ModuleTypeTestCase(TestCase):
    '''
        Defined class ModuleTypeTestCase with attribute(s) and method(s).
        Created test cases for checking functionalities of ModuleType.
        ModuleType unittests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_pre_process_module - Test pre-process module.
                | test_is_source_module - Test is source module.
                | test_is_build_module - Test is build module.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_pre_process_src_module(self) -> None:
        '''Test pre-process module.'''
        self.assertEqual(
            ModuleType.pre_process_module(
                'app', 'simple_test', 'test.c'
            ), 'test.c'
        )

    def test_pre_process_lib_h_module(self) -> None:
        '''Test pre-process module.'''
        self.assertEqual(
            ModuleType.pre_process_module(
                'lib', 'simple_test', 'simple_test.h'
            ), 'simple_test.h'
        )

    def test_pre_process_lib_c_module(self) -> None:
        '''Test pre-process module.'''
        self.assertEqual(
            ModuleType.pre_process_module(
                'lib', 'simple_test', 'simple_test.c'
            ), 'simple_test.c'
        )

    def test_pre_process_module_lib(self) -> None:
        '''Test pre-process module.'''
        self.assertEqual(
            ModuleType.pre_process_module(
                'lib', 'simple_test', 'Makefile'
            ), 'Makefile'
        )

    def test_pre_process_module_app(self) -> None:
        '''Test pre-process module.'''
        self.assertEqual(
            ModuleType.pre_process_module(
                'app', 'simple_test', 'Makefile'
            ), 'Makefile'
        )

    def test_is_source_module(self) -> None:
        '''Test is source module.'''
        app_module = 'simple_test.c'
        self.assertTrue(ModuleType.is_source_module(app_module))

    def test_is_build_module(self) -> None:
        '''Test is build module.'''
        build_module = 'Makefile'
        self.assertTrue(ModuleType.is_build_module(build_module))


if __name__ == '__main__':
    main()
