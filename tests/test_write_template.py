# -*- coding: UTF-8 -*-

'''
 Module
     test_write_template.py
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
     Defined class WriteTemplateTestCase with attribute(s) and method(s).
     Created test cases for checking functionalities of WriteTemplate.
 Execute
     python3 -m unittest -v test_write_template
'''

import sys
import unittest
from os.path import dirname, abspath

try:
    from gen_avr8.pro.read_template import ReadTemplate
    from gen_avr8.pro.write_template import WriteTemplate
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


class WriteTemplateTestCase(unittest.TestCase):
    '''
        Defined class WriteTemplateTestCase with attribute(s) and method(s).
        Created test cases for checking functionalities of WriteTemplate.
        It defines:

            :attributes:
                | template_writer - Project template reader.
                | template_modules - Project templates.
            :methods:
                | setUp - call before test case.
                | tearDown - call after test case.
                | test_read - Test write templates.
    '''

    def setUp(self):
        '''Call before test case.'''
        self.template_writer = WriteTemplate()
        self.template_reader = ReadTemplate()
        self.template_modules = [
            '{0}/{1}'.format(
                dirname(abspath(__file__)),
                '../gen_avr8/conf/template/app/Makefile.template'
            ),
            '{0}/{1}'.format(
                dirname(abspath(__file__)),
                '../gen_avr8/conf/template/app/module.template'
            )
        ]

    def tearDown(self):
        '''Call after test case.'''
        self.template_writer = None
        self.template_reader = None
        self.template_modules = None

    def test_read(self):
        '''Test read templates.'''
        project_setup = {
            'name': 'simple_test',
            'type': 'app',
            'mcu': 'atmega8',
            'osc': '16000000UL',
        }
        self.template_writer.pro_dir = project_setup['name']
        for template_module in self.template_modules:
            project_setup['template'] = self.template_reader.read(
                template_module
            )
            if 'Makefile' in template_module:
                project_setup['module'] = 'Makefile'
            else:
                project_setup['module'] = 'empty_test.c'

            self.assertEqual(
                self.template_writer.write(project_setup), True
            )


if __name__ == '__main__':
    unittest.main()
