# -*- coding: UTF-8 -*-

'''
Module
    mcu_selector.py
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
    Defines class MCUSelector with attribute(s) and method(s).
    Selects MCU target for generation process of project structure.
'''

import sys
from typing import Dict, List, Optional
from os.path import dirname, realpath

try:
    from ats_utilities.console_io.error import error_message
    from ats_utilities.config_io.file_check import FileCheck
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config_io.yaml.yaml2object import Yaml2Object
except ImportError as ats_error_message:
    # Force close python ATS ##################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/gen_avr8'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_avr8/blob/dev/LICENSE'
__version__ = '2.6.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class MCUSelector(FileCheck):
    '''
        Defines class MCUSelector with attribute(s) and method(s).
        Selects MCU target for generation process of project structure.

        It defines:

            :attributes:
                | _GEN_VERBOSE - Console text indicator for process-phase.
                | _MCU_LIST - Configuration file path with suported MCU list.
                | _mcu_list - Microcontroller list.
            :methods:
                | __init__ - Initials MCUSelector constructor.
                | get_mcu_list - Gets for MCU list object.
                | choose_mcu - Selects MCU target.
    '''

    _GEN_VERBOSE: str = 'GEN_AVR8::PRO::MCU_SELECTOR'
    _MCU_LIST: str = '/../conf/mcu.yaml'

    def __init__(self, verbose: bool = False) -> None:
        '''
            Initials MCUSelector constructor.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        super().__init__(verbose)
        verbose_message(
            verbose, [f'{self._GEN_VERBOSE.lower()} init MCU selector']
        )
        mcu_list: str = f'{dirname(realpath(__file__))}{self._MCU_LIST}'
        self.check_path(mcu_list, verbose)
        self.check_mode('r', verbose)
        self.check_format(mcu_list, 'yaml', verbose)
        self._mcu_list: Optional[List[str]] = None
        if self.is_file_ok():
            yml2obj: Optional[Yaml2Object] = Yaml2Object(mcu_list)
            mcu_cfg: Optional[Dict[str, str]] = yml2obj.read_configuration()
            if bool(mcu_cfg) and 'mcu' in mcu_cfg:
                self._mcu_list = mcu_cfg['mcu'].split(' ')

    def get_mcu_list(self) -> Optional[List[str]]:
        '''
            Gets for MCU list object.

            :return: MCU list | None
            :rtype: <Optional[List[str]]>
            :exceptions: None
        '''
        return self._mcu_list

    def choose_mcu(self, verbose: bool = False) -> Optional[str]:
        '''
            Selects MCU target.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: MCU name | None
            :rtype: <Optional[str]>
            :exceptions: None
        '''
        verbose_message(verbose, [f'{self._GEN_VERBOSE.lower()} select MCU'])
        mcu_name: Optional[str] = None
        if self._mcu_list:
            while True:
                mcu_name_index: int = -1
                print(f'{"#" * 30}\n')
                for index, item in enumerate(self._mcu_list):
                    print(f"\t{index}: {item}")
                print(f'{"#" * 30}\n')
                mcu_name_index = int(input(' select MCU: '))
                if mcu_name_index not in range(len(self._mcu_list)):
                    error_message(
                        [f'{self._GEN_VERBOSE.lower()} not an option']
                    )
                    continue
                else:
                    mcu_name = self._mcu_list[mcu_name_index]
                    break
        return mcu_name
