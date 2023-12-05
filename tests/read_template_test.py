# -*- coding: UTF-8 -*-

'''
Module
    read_template_test.py
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
    Defines class ReadTemplateTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of ReadTemplate.
Execute
    python3 -m unittest -v read_template_test
'''

import sys
from typing import List
from unittest import TestCase, main
from os.path import dirname, abspath

try:
    from gen_avr8.pro.read_template import ReadTemplate
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


class ReadTemplateTestCase(TestCase):
    '''
        Defined class ReadTemplateTestCase with attribute(s) and method(s).
        Created test cases for checking functionalities of ReadTemplate.
        ReadTemplate unittests.

        It defines:

            :attributes:
                | template_reader - Project template reader.
                | template_modules - Project templates.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_read - Test read templates.
    '''

    _MAKEFILE: str = '../gen_avr8/conf/template/app/Makefile.template'
    _MODULE: str = '../gen_avr8/conf/template/app/module.template'

    def setUp(self) -> None:
        '''Call before test case.'''
        self.template_reader: ReadTemplate | None = ReadTemplate()
        self.template_modules: List[str] | None = [
            f'{dirname(abspath(__file__))}/{self._MAKEFILE}',
            f'{dirname(abspath(__file__))}/{self._MODULE}'
        ]

    def tearDown(self) -> None:
        '''Call after test case.'''
        self.template_reader = None
        self.template_modules = None

    def test_read(self) -> None:
        '''Test read templates.'''
        if self.template_reader and self.template_modules:
            for template_module in self.template_modules:
                self.assertTrue(
                    self.template_reader.read(template_module) is not None
                )


if __name__ == '__main__':
    main()
