# -*- coding: UTF-8 -*-

'''
 Module
     test_template_type.py
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
     Defined class TemplateTypeTestCase with attribute(s) and method(s).
     Created test cases for checking functionalities of TemplateType.
 Execute
     python3 -m unittest -v test_template_type
'''

import sys
import unittest
from os.path import exists, dirname, realpath

try:
    from gen_avr8.pro.template_type import TemplateType
except ImportError as test_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, test_error_message)
    sys.exit(MESSAGE)  # Force close python test ############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2022, https://vroncevic.github.io/gen_avr8'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_avr8/blob/dev/LICENSE'
__version__ = '2.2.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TemplateTypeTestCase(unittest.TestCase):
    '''
        Defined class TemplateTypeTestCase with attribute(s) and method(s).
        Created test cases for checking functionalities of TemplateType.
        It defines:

            :attributes:
                | app_template - Project template dir path.
                | lib_template - Project template dir path.
            :methods:
                | setUp - call before test case.
                | tearDown - call after test case.
                | test_template_type_app - Test app template type check.
                | test_template_type_lib - Test lib template type check.
                | test_setup_template_app - Test setup template app check.
                | test_setup_template_lib - Test setup template lib check.
                | test_setup_app_dir - Test app template dir check.
                | test_setup_lib_dir - Test lib template dir check.
    '''

    def setUp(self):
        '''Call before test case.'''
        self.app_template = '{0}/{1}/{2}'.format(
            dirname(realpath(__file__)),
            '../gen_avr8/conf/template',
            TemplateType.APP_TEMPLATE
        )
        self.lib_template = '{0}/{1}/{2}'.format(
            dirname(realpath(__file__)),
            '../gen_avr8/conf/template',
            TemplateType.LIB_TEMPLATE
        )

    def tearDown(self):
        '''Call after test case.'''
        self.app_template = None
        self.lib_template = None

    def test_template_type_app(self):
        '''Test app template type check.'''
        self.assertEqual(TemplateType.check_template_type('app'), True)

    def test_template_type_lib(self):
        '''Test lib template type check.'''
        self.assertEqual(TemplateType.check_template_type('lib'), True)

    def test_setup_template_app(self):
        '''Test setup template app check.'''
        self.assertEqual(
            TemplateType.setup_template_type('app'),
            TemplateType.TEMPLATE_TYPE['app']
        )

    def test_setup_template_lib(self):
        '''Test setup template lib check.'''
        self.assertEqual(
            TemplateType.setup_template_type('lib'),
            TemplateType.TEMPLATE_TYPE['lib']
        )

    def test_setup_app_dir(self):
        '''Test app template dir check.'''
        self.assertEqual(exists(self.app_template), True)

    def test_setup_lib_dir(self):
        '''Test lib template dir check.'''
        self.assertEqual(exists(self.lib_template), True)


if __name__ == '__main__':
    unittest.main()
