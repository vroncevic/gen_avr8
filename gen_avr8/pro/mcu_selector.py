# -*- coding: UTF-8 -*-

'''
 Module
     mcu_selector.py
 Copyright
     Copyright (C) 2019 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Define class MCUSelector with attribute(s) and method(s).
     Selecting MCU target for generating process of project structure.
'''

import sys

try:
    from pathlib import Path
    from ats_utilities.console_io.error import error_message
    from ats_utilities.config_io.base_check import FileChecking
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config_io.yaml.yaml2object import Yaml2Object
except ImportError as error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2020, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.4.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class MCUSelector(FileChecking):
    '''
        Define class MCUSelector with attribute(s) and method(s).
        Selecting MCU target for generating process of project structure.
        It defines:

            :attributes:
                | __slots__ - Setting class slots.
                | VERBOSE - Console text indicator for current process-phase.
                | __MCU_LIST - Configuration file with MCU list.
                | __mcu_list - MCU list.
            :methods:
                | __init__ - Initial constructor.
                | get_mcu_list - Getter for MCU list object.
                | choose_mcu - Select MCU target.
    '''

    __slots__ = ('VERBOSE', '__MCU_LIST', '__mcu_list')
    VERBOSE = 'GEN_AVR8::PRO::MCU_SELECTOR'
    __MCU_LIST = '/../conf/mcu.yaml'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        verbose_message(MCUSelector.VERBOSE, verbose, 'init MCU selector')
        FileChecking.__init__(self, verbose=verbose)
        mcu_list = '{0}{1}'.format(
            Path(__file__).parent, MCUSelector.__MCU_LIST
        )
        self.check_path(file_path=mcu_list, verbose=verbose)
        self.check_mode(file_mode='r', verbose=verbose)
        self.check_format(
            file_path=mcu_list, file_format='yaml', verbose=verbose
        )
        if self.is_file_ok():
            yml2obj = Yaml2Object(mcu_list)
            mcu_cfg = yml2obj.read_configuration()
            self.__mcu_list = mcu_cfg['mcu'].split(' ')
        else:
            self.__mcu_list = None

    def get_mcu_list(self):
        '''
            Getter for MCU list object.

            :return: MCU list | None.
            :rtype: <list> | <NoneType>
            :exceptions: None
        '''
        return self.__mcu_list

    def choose_mcu(self, verbose=False):
        '''
            Select MCU target.

            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :return: MCU name | None.
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        verbose_message(MCUSelector.VERBOSE, verbose, 'select MCU')
        mcu_name_index, mcu_name = -1, None
        if bool(self.__mcu_list):
            while True:
                print('{0}\n'.format('#' * 30))
                for index in range(len(self.__mcu_list)):
                    print('\t{0}: {1}'.format(index, self.__mcu_list[index]))
                print('{0}\n'.format('#' * 30))
                try:
                    mcu_name_index = int(raw_input(' select MCU: '))
                except NameError:
                    mcu_name_index = int(input(' select MCU: '))
                if mcu_name_index not in range(len(self.__mcu_list)):
                    error_message(
                        MCUSelector.VERBOSE, 'not an appropriate choice'
                    )
                else:
                    mcu_name = self.__mcu_list[mcu_name_index]
                    break
        return mcu_name
