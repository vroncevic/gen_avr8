# -*- coding: UTF-8 -*-

'''
 Module
     osc_selector.py
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
     Defined class OSCSelector with attribute(s) and method(s).
     Selecting FOSC for generating process of project structure.
'''

import sys

try:
    from pathlib import Path
    from ats_utilities.console_io.error import error_message
    from ats_utilities.config_io.base_check import FileChecking
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config_io.yaml.yaml2object import Yaml2Object
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.6.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class OSCSelector(FileChecking):
    '''
        Defined class OSCSelector with attribute(s) and method(s).
        Selecting FOSC for generating process of project structure.
        It defines:

            :attributes:
                | __slots__ - Setting class slots.
                | VERBOSE - Console text indicator for current process-phase.
                | __FOSC_LIST - Configuration file with FOSC list.
                | __fosc_list - FOSC list.
            :methods:
                | __init__ - Initial constructor.
                | get_fosc_list - Getter for FOSC list object.
                | choose_osc - Select FOSC for target.
                | __str__ - Dunder method for OSCSelector.
    '''

    __slots__ = ('VERBOSE', '__FOSC_LIST', '__fosc_list')
    VERBOSE = 'GEN_AVR8::PRO::OSC_SELECTOR'
    __FOSC_LIST = '/../conf/fosc.yaml'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        verbose_message(OSCSelector.VERBOSE, verbose, 'init form selector')
        FileChecking.__init__(self, verbose=verbose)
        fosc_list = '{0}{1}'.format(
            Path(__file__).parent, OSCSelector.__FOSC_LIST
        )
        self.check_path(file_path=fosc_list, verbose=verbose)
        self.check_mode(file_mode='r', verbose=verbose)
        self.check_format(
            file_path=fosc_list, file_format='yaml', verbose=verbose
        )
        if self.is_file_ok():
            yml2obj = Yaml2Object(fosc_list)
            fosc_cfg = yml2obj.read_configuration()
            self.__fosc_list = fosc_cfg['osc'].split(' ')
        else:
            self.__fosc_list = None

    def get_fosc_list(self):
        '''
            Getter for FOSC list object.

            :return: FOSC Configuration | None.
            :rtype: <list> | <NoneType>
            :exceptions: None
        '''
        return self.__fosc_list

    def choose_osc(self, verbose=False):
        '''
            Select FOSC for target.

            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :return: FOSC | None.
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        verbose_message(OSCSelector.VERBOSE, verbose, 'select FOSC')
        fosc_name_index, fosc_name = -1, None
        if bool(self.__fosc_list):
            while True:
                print('{0}\n'.format('#' * 30))
                for index in range(len(self.__fosc_list)):
                    print('\t{0}: {1}'.format(index, self.__fosc_list[index]))
                print('{0}\n'.format('#' * 30))
                try:
                    fosc_name_index = int(raw_input(' select FOSC: '))
                except NameError:
                    fosc_name_index = int(input(' select FOSC: '))
                if fosc_name_index not in range(len(self.__fosc_list)):
                    error_message(
                        OSCSelector.VERBOSE, 'not an appropriate choice'
                    )
                else:
                    fosc_name = self.__fosc_list[fosc_name_index]
                    break
        return fosc_name

    def __str__(self):
        '''
            Dunder method for OSCSelector.

            :return: Object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2})'.format(
            self.__class__.__name__, FileChecking.__str__(self),
            str(self.__fosc_list)
        )
