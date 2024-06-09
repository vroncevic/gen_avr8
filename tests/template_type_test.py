# -*- coding: UTF-8 -*-

'''
Module
    template_type_test.py
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
    Defines class TemplateTypeTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of TemplateType.
Execute
    python3 -m unittest -v template_type_test
'''

import sys
from typing import List
from unittest import TestCase, main
from os.path import exists, dirname, realpath

try:
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_value_error import ATSValueError
    from gen_avr8.pro.template_type import TemplateType
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/gen_avr8'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_avr8/blob/dev/LICENSE'
__version__ = '2.6.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TemplateTypeTestCase(TestCase):
    '''
        Defines class TemplateTypeTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of TemplateType.
        TemplateType unit tests.

        It defines:

            :attributes:
                | _CONF - Template directory.
                | app_template - Project template dir path.
                | lib_template - Project template dir path.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_template_type_app - Test app template type.
                | test_template_type_lib - Test lib template type.
                | test_template_type_none - Test app template type None.
                | test_setup_template_app - Test setup template app.
                | test_setup_template_lib - Test setup template lib.
                | test_setup_template_empty - Test setup template lib empty.
                | test_setup_template_not_supported - Template not supported.
                | test_setup_app_dir - Test app template dir.
                | test_setup_lib_dir - Test lib template dir.
    '''

    _CONF: str = '../gen_avr8/conf/template'

    def setUp(self) -> None:
        '''Call before test case'''
        cwd: str = dirname(realpath(__file__))
        self.app_template: str | None = f'{cwd}/{self._CONF}/app'
        self.lib_template: str | None = f'{cwd}/{self._CONF}/lib'

    def tearDown(self) -> None:
        '''Call after test case'''
        self.app_template = None
        self.lib_template = None

    def test_template_type_app(self) -> None:
        '''Test app template type'''
        self.assertTrue(TemplateType.check_template_type('app'))

    def test_template_type_lib(self) -> None:
        '''Test lib template type'''
        self.assertTrue(TemplateType.check_template_type('lib'))

    def test_template_type_none(self) -> None:
        '''Test app template type None'''
        with self.assertRaises(ATSTypeError):
            TemplateType.check_template_type(None)

    def test_setup_template_app(self) -> None:
        '''Test setup template app'''
        self.assertEqual(
            TemplateType.setup_template_type('app'),
            'project_app.yaml'
        )

    def test_setup_template_lib(self) -> None:
        '''Test setup template lib'''
        self.assertEqual(
            TemplateType.setup_template_type('lib'),
            'project_lib.yaml'
        )

    def test_setup_template_empty(self) -> None:
        '''Test setup template lib empty'''
        with self.assertRaises(ATSValueError):
            TemplateType.setup_template_type('')

    def test_setup_template_not_supported(self) -> None:
        '''Template not supported'''
        self.assertIsNone(TemplateType.setup_template_type('ext'))

    def test_setup_app_dir(self) -> None:
        '''Test app template dir'''
        if self.app_template:
            self.assertTrue(exists(self.app_template))

    def test_setup_lib_dir(self) -> None:
        '''Test lib template dir'''
        if self.lib_template:
            self.assertTrue(exists(self.lib_template))


if __name__ == '__main__':
    main()
