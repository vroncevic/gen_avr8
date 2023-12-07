# -*- coding: UTF-8 -*-

'''
Module
    write_template_test.py
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
    Defines class WriteTemplateTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of WriteTemplate.
Execute
    python3 -m unittest -v write_template_test
'''

import sys
from typing import List, Dict
from unittest import TestCase, main
from os.path import dirname, abspath

try:
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from gen_avr8.pro.read_template import ReadTemplate
    from gen_avr8.pro.write_template import WriteTemplate
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


class WriteTemplateTestCase(TestCase):
    '''
        Defines class WriteTemplateTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of WriteTemplate.
        WriteTemplate unittests.

        It defines:

            :attributes:
                | _MAKEFILE - Template for Makefile.
                | _MODULE - Template for module.
                | template_writer - Project template reader.
                | template_modules - Project templates.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_set_none_pro_dir - Test set none pro dir.
                | test_get_pro_dir - Test get pro dir.
                | test_check_module_none - Test check module none.
                | test_write_none - Test check write none.
                | test_read_write - Test read write templates.
    '''

    _MAKEFILE: str = '../gen_avr8/conf/template/app/Makefile.template'
    _MODULE: str = '../gen_avr8/conf/template/app/module.template'

    def setUp(self) -> None:
        '''Call before test case'''
        self.template_writer: WriteTemplate | None = WriteTemplate()
        self.template_reader: ReadTemplate | None = ReadTemplate()
        cwd: str = dirname(abspath(__file__))
        self.template_modules: List[str] | None = [
            f'{cwd}/{self._MAKEFILE}',
            f'{cwd}/{self._MODULE}'
        ]

    def tearDown(self) -> None:
        '''Call after test case'''
        self.template_writer = None
        self.template_reader = None
        self.template_modules = None

    def test_set_none_pro_dir(self) -> None:
        '''Test set none pro dir'''
        with self.assertRaises(ATSTypeError):
            if self.template_writer:
                self.template_writer.pro_dir = None

    def test_get_pro_dir(self) -> None:
        '''Test get pro dir'''
        pro_dir: str = 'new_pro'
        if self.template_writer:
            self.template_writer.pro_dir = pro_dir
            self.assertIsNotNone(self.template_writer.pro_dir)

    def test_check_module_none(self) -> None:
        '''Test check module none'''
        with self.assertRaises(ATSTypeError):
            if self.template_writer:
                self.template_writer.check_module(None)

    def test_write_none(self) -> None:
        '''Test check write none'''
        with self.assertRaises(ATSTypeError):
            if self.template_writer:
                self.template_writer.write(None)  # type: ignore

    def test_read_write(self) -> None:
        '''Test read write templates'''
        project_setup: Dict[str, str] | None = {
            'name': 'simple_test',
            'type': 'app',
            'mcu': 'atmega8',
            'osc': '16000000UL'
        }
        if self.template_writer and self.template_modules:
            self.template_writer.pro_dir = project_setup['name']
            for template_module in self.template_modules:
                if project_setup and self.template_reader:
                    template: str | None = self.template_reader.read(
                        template_module
                    )
                    project_setup['template'] = str(template)
                    if 'Makefile' in template_module:
                        project_setup['module'] = 'Makefile'
                    else:
                        project_setup['module'] = 'empty_test.c'
                    self.assertTrue(self.template_writer.write(project_setup))


if __name__ == '__main__':
    main()
