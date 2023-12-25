# -*- coding: UTF-8 -*-

'''
Module
    template_dir_test.py
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
    Defines class TemplateDirTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of TemplateDir.
Execute
    python3 -m unittest -v template_dir_test
'''

import sys
from typing import List
from unittest import TestCase, main
from os.path import exists

try:
    from gen_avr8.pro.template_dir import TemplateDir
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/gen_avr8'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_avr8/blob/dev/LICENSE'
__version__ = '2.5.9'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TemplateDirTestCase(TestCase):
    '''
        Defines class TemplateDirTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of TemplateDir.
        TemplateDir unit tests.

        It defines:

            :attributes:
                | config_dir - Project configuraiton dir path.
                | template_dir - Project template dir path.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_is_app_dir_name_ok - Test app dir name check.
                | test_is_lib_dir_name_ok - Test lib dir name check.
                | test_setup_conf_dir - Test conf dir check.
                | test_setup_template_dir - Test template dir check.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.config_dir: str | None = TemplateDir.setup_conf_dir()
        self.template_dir: str | None = TemplateDir.setup_template_dir()

    def tearDown(self) -> None:
        '''Call after test case.'''
        self.config_dir = None
        self.template_dir = None

    def test_is_app_dir_name_ok(self) -> None:
        '''Test app dir name check.'''
        self.assertTrue(TemplateDir.check_dir('/../conf/template/app/'))

    def test_is_lib_dir_name_ok(self) -> None:
        '''Test lib dir name check.'''
        self.assertTrue(TemplateDir.check_dir('/../conf/template/lib/'))

    def test_setup_conf_dir(self) -> None:
        '''Test conf dir check.'''
        if self.config_dir:
            self.assertTrue(exists(self.config_dir))

    def test_setup_template_dir(self) -> None:
        '''Test template dir check.'''
        if self.template_dir:
            self.assertTrue(exists(self.template_dir))


if __name__ == '__main__':
    main()
