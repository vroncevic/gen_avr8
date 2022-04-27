# -*- coding: UTF-8 -*-

'''
 Module
     template_dir.py
 Copyright
     Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Defined class TemplateDir with attribute(s) and method(s).
     Created API for checking project template directory.
'''

import sys
from os.path import isdir, dirname, realpath

try:
    from ats_utilities.console_io.verbose import verbose_message
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, https://vroncevic.github.io/gen_avr8'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_avr8/blob/dev/LICENSE'
__version__ = '2.4.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TemplateDir:
    '''
        Defined class TemplateDir with attribute(s) and method(s).
        Created API for checking project template directory.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
                | CONF_DIR - configuration directory path.
                | TEMPLATE_DIR - template directory path.
            :methods:
                | check_dir - check project directory.
                | setup_conf_dir - setup configuration directory.
                | setup_template_dir - setup template directory.
                | __str__ - dunder method for TemplateDir.
    '''

    GEN_VERBOSE = 'GEN_AVR8::PRO::TEMPLATE_DIR'
    CONF_DIR, TEMPLATE_DIR = '/../conf/', '/../conf/template/'

    @classmethod
    def check_dir(cls, target_dir, verbose=False):
        '''
            Checking project directory.

            :param target_dir: target directory to be checked.
            :type target_dir: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: boolean status, True directory ok | False.
            :rtype: <bool>
            :exceptions: None
        '''
        verbose_message(cls.GEN_VERBOSE, verbose, 'check project directory')
        return isdir('{0}{1}'.format(dirname(realpath(__file__)), target_dir))

    @classmethod
    def setup_conf_dir(cls, verbose=False):
        '''
            Setup configuration directory.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: template directory | None.
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        configuration_dir = None
        if cls.check_dir(target_dir=cls.CONF_DIR, verbose=verbose):
            configuration_dir = '{0}{1}'.format(
                dirname(realpath(__file__)), cls.CONF_DIR
            )
            verbose_message(
                cls.GEN_VERBOSE, verbose, 'conf directory', configuration_dir
            )
        return configuration_dir

    @classmethod
    def setup_template_dir(cls, verbose=False):
        '''
            Setup template directory.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: template directory | None.
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        template_dir = None
        if cls.check_dir(target_dir=cls.TEMPLATE_DIR, verbose=verbose):
            template_dir = '{0}{1}'.format(
                dirname(realpath(__file__)), cls.TEMPLATE_DIR
            )
            verbose_message(
                cls.GEN_VERBOSE, verbose, 'template directory', template_dir
            )
        return template_dir

    def __str__(self):
        '''
            Dunder method for TemplateDir.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ()'.format(self.__class__.__name__)
