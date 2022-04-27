# -*- coding: UTF-8 -*-

'''
 Module
     test_template_dir.py
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
     Defined class TemplateDirTestCase with attribute(s) and method(s).
     Created test cases for checking functionalities of TemplateDir.
 Execute
     python3 -m unittest -v test_template_dir
'''

import sys
import unittest
from os.path import exists

try:
    from gen_avr8.pro.template_dir import TemplateDir
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


class TemplateDirTestCase(unittest.TestCase):
    '''
        Defined class TemplateDirTestCase with attribute(s) and method(s).
        Created test cases for checking functionalities of TemplateDir.
        It defines:

            :attributes:
                | config_dir - Project configuraiton dir path.
                | template_dir - Project template dir path.
            :methods:
                | setUp - call before test case.
                | tearDown - call after test case.
                | test_is_app_dir_name_ok - Test app dir name check.
                | test_is_lib_dir_name_ok - Test lib dir name check.
                | test_setup_conf_dir - Test conf dir check.
                | test_setup_template_dir - Test template dir check.
    '''

    def setUp(self):
        '''Call before test case.'''
        self.config_dir = TemplateDir.setup_conf_dir()
        self.template_dir = TemplateDir.setup_template_dir()

    def tearDown(self):
        '''Call after test case.'''
        self.config_dir = None
        self.template_dir = None

    def test_is_app_dir_name_ok(self):
        '''Test app dir name check.'''
        self.assertEqual(
            TemplateDir.check_dir('/../conf/template/app/'), True
        )

    def test_is_lib_dir_name_ok(self):
        '''Test lib dir name check.'''
        self.assertEqual(
            TemplateDir.check_dir('/../conf/template/lib/'), True
        )

    def test_setup_conf_dir(self):
        '''Test conf dir check.'''
        self.assertEqual(exists(self.config_dir), True)

    def test_setup_template_dir(self):
        '''Test template dir check.'''
        self.assertEqual(exists(self.template_dir), True)


if __name__ == '__main__':
    unittest.main()
