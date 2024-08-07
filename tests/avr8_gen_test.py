# -*- coding: UTF-8 -*-

'''
Module
    avr8_setup_test.py
Copyright
    Copyright (C) 2018 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines class GenAVR8TestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of GenAVR8.
Execute
    python3 -m unittest -v avr8_setup_test
'''

import sys
from os import makedirs, rmdir, getcwd
from typing import Any, List, Optional
from unittest import TestCase, main
from unittest.mock import patch

try:
    from gen_avr8 import GenAVR8
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/gen_avr8'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_avr8/blob/dev/LICENSE'
__version__ = '2.6.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenAVR8TestCase(TestCase):
    '''
        Defines class GenAVR8TestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of GenAVR8.
        GenAVR8 unitteests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_create - Test create (not None).
                | test_process_no_args - Test for no args.
                | test_process_missing_args - Test for missing args.
                | test_pro_dir_already_exists - Test pro dir exists.
                | test_process_wrong_args - Test wrong args.
                | test_process - Test success process.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_create(self) -> None:
        '''Test create (not None)'''
        avr_gen: Optional[GenAVR8] = GenAVR8()
        self.assertIsNotNone(avr_gen)

    def test_process_no_args(self) -> None:
        '''Test for no args'''
        avr_gen: Optional[GenAVR8] = GenAVR8()
        if avr_gen:
            self.assertIsInstance(avr_gen, GenAVR8)
            self.assertFalse(avr_gen.process())

    def test_process_missing_args(self) -> None:
        '''Test for missing args'''
        sys.argv.clear()
        avr_gen: Optional[GenAVR8] = GenAVR8()
        if avr_gen:
            self.assertIsInstance(avr_gen, GenAVR8)
            self.assertFalse(avr_gen.process())

    def test_pro_dir_already_exists(self) -> None:
        '''Test pro dir exists'''
        sys.argv.clear()
        sys.argv.insert(0, '-n')
        sys.argv.insert(1, 'tester2')
        sys.argv.insert(2, '-t')
        sys.argv.insert(3, 'app')
        makedirs(f'{getcwd()}/tester2', exist_ok=False)
        avr_gen: Optional[GenAVR8] = GenAVR8()
        if avr_gen:
            self.assertIsInstance(avr_gen, GenAVR8)
            self.assertFalse(avr_gen.process())
        rmdir('tester2')

    def test_process_wrong_args(self) -> None:
        '''Test wrong args'''
        sys.argv.clear()
        sys.argv.insert(0, '-n')
        sys.argv.insert(1, 'tester')
        sys.argv.insert(2, '-z')
        sys.argv.insert(3, 'app')
        avr_gen: Optional[GenAVR8] = GenAVR8()
        if avr_gen:
            self.assertIsInstance(avr_gen, GenAVR8)
            self.assertFalse(avr_gen.process())

    @patch('builtins.input', side_effect=['37', '9'])
    def test_process(self, mock_input: Any) -> None:
        '''Test success process'''
        sys.argv.clear()
        sys.argv.insert(0, '-n')
        sys.argv.insert(1, 'tester')
        sys.argv.insert(2, '-t')
        sys.argv.insert(3, 'app')
        avr_gen: Optional[GenAVR8] = GenAVR8()
        if avr_gen and mock_input:
            self.assertIsInstance(avr_gen, GenAVR8)
            self.assertTrue(avr_gen.process())


if __name__ == '__main__':
    main()
