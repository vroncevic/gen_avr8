# -*- coding: UTF-8 -*-

'''
 Module
     mcu_selector.py
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
     Defined class MCUSelector with attribute(s) and method(s).
     Selecting MCU target for generating process of project structure.
'''

import sys
from os.path import dirname, realpath

try:
    from ats_utilities.console_io.error import error_message
    from ats_utilities.config_io.base_check import FileChecking
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config_io.yaml.yaml2object import Yaml2Object
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


class MCUSelector(FileChecking):
    '''
        Defined class MCUSelector with attribute(s) and method(s).
        Selecting MCU target for generating process of project structure.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
                | MCU_LIST - configuration file with MCU list.
                | __mcu_list - MCU list.
            :methods:
                | __init__ - initial constructor.
                | get_mcu_list - getter for MCU list object.
                | choose_mcu - select MCU target.
                | __str__ - dunder method for MCUSelector.
    '''

    GEN_VERBOSE = 'GEN_AVR8::PRO::MCU_SELECTOR'
    MCU_LIST = '/../conf/mcu.yaml'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        FileChecking.__init__(self, verbose=verbose)
        verbose_message(MCUSelector.GEN_VERBOSE, verbose, 'init MCU selector')
        mcu_list = '{0}{1}'.format(
            dirname(realpath(__file__)), MCUSelector.MCU_LIST
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

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: MCU name | None.
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        verbose_message(MCUSelector.GEN_VERBOSE, verbose, 'select MCU')
        mcu_name_index, mcu_name = -1, None
        if bool(self.__mcu_list):
            while True:
                print('{0}\n'.format('#' * 30))
                for index in range(len(self.__mcu_list)):
                    print('\t{0}: {1}'.format(index, self.__mcu_list[index]))
                print('{0}\n'.format('#' * 30))
                mcu_name_index = int(input(' select MCU: '))
                if mcu_name_index not in range(len(self.__mcu_list)):
                    error_message(
                        MCUSelector.GEN_VERBOSE, 'not an appropriate choice'
                    )
                else:
                    mcu_name = self.__mcu_list[mcu_name_index]
                    break
        return mcu_name

    def __str__(self):
        '''
            Dunder method for MCUSelector.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2})'.format(
            self.__class__.__name__, FileChecking.__str__(self),
            str(self.__mcu_list)
        )
