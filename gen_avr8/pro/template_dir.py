# -*- coding: UTF-8 -*-

'''
 Module
     template_dir.py
 Copyright
     Copyright (C) 2021 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Define class TemplateDir with method(s).
     Check project template directory.
'''

import sys
from os.path import isdir

try:
    from pathlib import Path
    from ats_utilities.console_io.verbose import verbose_message
except ImportError as error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2021, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.4.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TemplateDir(object):
    '''
        Define class TemplateDir with attribute(s) and method(s).
        Check project template directory.
        It defines:

            :attributes:
                | __slots__ - Setting class slots.
                | VERBOSE - Console text indicator for current process-phase.
                | __CONF_DIR - Configuration directory path.
                | __TEMPLATE_DIR - Template directory path.
            :methods:
                | check_dir - Check project directory.
                | setup_conf_dir - Setup configuration directory.
                | setup_template_dir - Setup template directory.
    '''

    __slots__ = ('VERBOSE', '__CONF_DIR', '__TEMPLATE_DIR')
    VERBOSE = 'GEN_AVR8::PRO::TEMPLATE_DIR'
    __CONF_DIR, __TEMPLATE_DIR = '/../conf/', '/../conf/template/'

    @classmethod
    def check_dir(cls, target_dir, verbose=False):
        '''
            Checking project directory.

            :param target_dir: Target directory to be checked.
            :type target_dir: <str>
            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :return: True directory ok else False.
            :rtype: <bool>
            :exceptions: None
        '''
        verbose_message(
            cls.VERBOSE, verbose, 'check project directory'
        )
        return isdir(
            '{0}{1}'.format(
                Path(__file__).parent, target_dir
            )
        )

    @classmethod
    def setup_conf_dir(cls, verbose=False):
        '''
            Setup configuration directory.

            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :return: Template directory | None.
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        configuration_dir = None
        if cls.check_dir(target_dir=cls.__CONF_DIR, verbose=verbose):
            configuration_dir = '{0}{1}'.format(
                Path(__file__).parent, cls.__CONF_DIR
            )
            verbose_message(
                cls.VERBOSE, verbose, 'conf directory', configuration_dir
            )
        return configuration_dir

    @classmethod
    def setup_template_dir(cls, verbose=False):
        '''
            Setup template directory.

            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :return: Template directory | None.
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        template_dir = None
        if cls.check_dir(target_dir=cls.__TEMPLATE_DIR, verbose=verbose):
            template_dir = '{0}{1}'.format(
                Path(__file__).parent, cls.__TEMPLATE_DIR
            )
            verbose_message(
                cls.VERBOSE, verbose, 'template directory', template_dir
            )
        return template_dir
