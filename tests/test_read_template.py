# -*- coding: UTF-8 -*-

'''
 Module
     test_read_template.py
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
     Defined class ReadTemplateTestCase with attribute(s) and method(s).
     Created test cases for checking functionalities of ReadTemplate.
 Execute
     python3 -m unittest -v test_read_template
'''

import sys
import unittest
from os.path import dirname, abspath

try:
    from gen_avr8.pro.read_template import ReadTemplate
except ImportError as test_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, test_error_message)
    sys.exit(MESSAGE)  # Force close python test ############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2022, https://vroncevic.github.io/gen_avr8'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_avr8/blob/dev/LICENSE'
__version__ = '1.3.3'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ReadTemplateTestCase(unittest.TestCase):
    '''
        Defined class ReadTemplateTestCase with attribute(s) and method(s).
        Created test cases for checking functionalities of ReadTemplate.
        It defines:

            :attributes:
                | template_reader - Project template reader.
                | template_modules - Project templates.
            :methods:
                | setUp - call before test case.
                | tearDown - call after test case.
                | test_read - Test read templates.
    '''

    def setUp(self):
        '''Call before test case.'''
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
        self.template_reader = None
        self.template_modules = None

    def test_read(self):
        '''Test read templates.'''
        for template_module in self.template_modules:
            self.assertEqual(
                self.template_reader.read(template_module) is not None, True
            )


if __name__ == '__main__':
    unittest.main()
