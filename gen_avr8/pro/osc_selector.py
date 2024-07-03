# -*- coding: UTF-8 -*-

'''
Module
    osc_selector.py
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
    Defines class OSCSelector with attribute(s) and method(s).
    Selects FOSC for generation process of project structure.
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


class OSCSelector(FileCheck):
    '''
        Defines class OSCSelector with attribute(s) and method(s).
        Selects FOSC for generation process of project structure.

        It defines:

            :attributes:
                | _GEN_VERBOSE - Console text indicator for process-phase.
                | _FOSC_LIST - Configuration file with FOSC list.
                | _fosc_list - FOSC list.
            :methods:
                | __init__ - Initials OSCSelector constructor.
                | get_fosc_list - Gets for FOSC list object.
                | choose_osc - Selects FOSC for target.
    '''

    _GEN_VERBOSE: str = 'GEN_AVR8::PRO::OSC_SELECTOR'
    _FOSC_LIST: str = '/../conf/fosc.yaml'

    def __init__(self, verbose: bool = False) -> None:
        '''
            Initials OSCSelector constructor.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        super().__init__(verbose)
        verbose_message(
            verbose, [f'{self._GEN_VERBOSE.lower()} init fosc selector']
        )
        fosc_list: str = f'{dirname(realpath(__file__))}{self._FOSC_LIST}'
        self.check_path(fosc_list, verbose)
        self.check_mode('r', verbose)
        self.check_format(fosc_list, 'yaml', verbose)
        self._fosc_list: Optional[List[str]] = None
        if self.is_file_ok():
            yml2obj: Optional[Yaml2Object] = Yaml2Object(fosc_list)
            fosc_cfg: Dict[str, str] | None = yml2obj.read_configuration()
            if bool(fosc_cfg) and 'osc' in fosc_cfg:
                self._fosc_list = fosc_cfg['osc'].split(' ')

    def get_fosc_list(self) -> Optional[List[str]]:
        '''
            Gets for FOSC list object.

            :return: FOSC configuration | None
            :rtype: <Optional[List[str]]>
            :exceptions: None
        '''
        return self._fosc_list

    def choose_osc(self, verbose: bool = False) -> Optional[str]:
        '''
            Select FOSC for target.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: FOSC | None
            :rtype: <Optional[str]>
            :exceptions: None
        '''
        verbose_message(verbose, [f'{self._GEN_VERBOSE.lower()} select FOSC'])
        fosc_name_index: int = -1
        fosc_name: Optional[str] = None
        if self._fosc_list:
            while True:
                print(f'{"#" * 30}\n')
                for index, item in enumerate(self._fosc_list):
                    print(f'\t{index}: {item}')
                print(f'{"#" * 30}\n')
                fosc_name_index = int(input(' select FOSC: '))
                if fosc_name_index not in range(len(self._fosc_list)):
                    error_message(
                        [f'{self._GEN_VERBOSE.lower()} not an option']
                    )
                    continue
                else:
                    fosc_name = self._fosc_list[fosc_name_index]
                    break
        return fosc_name
