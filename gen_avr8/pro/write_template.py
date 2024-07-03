# -*- coding: UTF-8 -*-

'''
Module
    write_template.py
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
    Defines class WriteTemplate with attribute(s) and method(s).
    Creates an API for writing template content with parameters.
'''

import sys
from typing import Dict, List, Optional
from os import getcwd, chmod, makedirs
from datetime import datetime
from string import Template

try:
    from ats_utilities.config_io.file_check import FileCheck
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from gen_avr8.pro.module_type import ModuleType
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


class WriteTemplate(FileCheck):
    '''
        Defines class WriteTemplate with attribute(s) and method(s).
        Creates an API for writing template content with parameters.

        It defines:

            :attributes:
                | _GEN_VERBOSE - Console text indicator for process-phase.
                | _pro_dir - Current project directory.
            :methods:
                | __init__ - Initials WriteTemplate constructor.
                | pro_dir - Property methods for set/get operations.
                | check_module - Checks project module.
                | write - Writes a template content to a project module.
    '''

    _GEN_VERBOSE: str = 'GEN_AVR8::PRO::WRITE_TEMPLATE'

    def __init__(self, verbose: bool = False) -> None:
        '''
            Initials WriteTemplate constructor.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        super().__init__(verbose)
        verbose_message(verbose, [f'{self._GEN_VERBOSE.lower()} init writer'])
        self._pro_dir: Optional[str] = None

    @property
    def pro_dir(self) -> Optional[str]:
        '''
            Property method for getting project dir.

            :return: Project dir | None
            :rtype: <Optional[str]>
            :exceptions: None
        '''
        return self._pro_dir

    @pro_dir.setter
    def pro_dir(self, pro_dir: Optional[str]) -> None:
        '''
            Property method for setting/creating project dir.

            :param pro_dir: Project dir | None
            :type pro_dir: <Optional[str]>
            :exceptions: ATSTypeError
        '''
        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = self.check_params([('str:pro_dir', pro_dir)])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        self._pro_dir = f'{getcwd()}/{pro_dir}'
        makedirs(f'{self._pro_dir}/build', exist_ok=True)

    def check_module(
        self, module: Optional[str], verbose: bool = False
    ) -> Optional[str]:
        '''
            Checks project module.

            :param module: Module name | None
            :type module: <Optional[str]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: 'build' | 'source'| None (wrong module name).
            :rtype: <Optional[str]>
            :exceptions: ATSTypeError
        '''
        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = self.check_params([('str:module', module)])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        is_source: bool = False
        is_build: bool = False
        module_type: Optional[str] = None
        is_source = ModuleType.is_source_module(module)
        is_build = ModuleType.is_build_module(module)
        if is_source and not is_build:
            module_type = 'source'
        if not is_source and is_build:
            module_type = 'build'
        verbose_message(
            verbose, [f'{self._GEN_VERBOSE.lower()} module type', module_type]
        )
        return module_type

    def write(self, pro_data: Dict[str, str], verbose: bool = False) -> bool:
        '''
            Writes a template content to a project module.

            :param pro_data: Project data
            :type pro_data: <Dict[str, str]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: True (success operation) | False
            :rtype: <bool>
            :exception: ATSTypeError
        '''
        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = self.check_params([
            ('dict:pro_data', pro_data)
        ])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        status = False
        module_type: Optional[str] = self.check_module(pro_data['module'])
        if bool(module_type):
            project: Dict[str, str] = {
                'PRO': f'{pro_data["name"]}',
                'MCU': f'{pro_data["mcu"]}',
                'OSC': f'{pro_data["osc"]}',
                'YEAR': f'{datetime.now().year}'
            }
            template = Template(pro_data['template'])
            if bool(template):
                module: Optional[str] = None
                if module_type == 'source':
                    module = f'{self._pro_dir}/{pro_data["module"]}'
                if module_type == 'build':
                    module = f'{self._pro_dir}/build/{pro_data["module"]}'
                if bool(module):
                    with open(module, 'w', encoding='utf-8') as module_file:
                        if bool(module_file):
                            verbose_message(
                                verbose,
                                [
                                    f'{self._GEN_VERBOSE.lower()} write ',
                                    module
                                ]
                            )
                            module_file.write(template.substitute(project))
                            chmod(module, 0o666)
                            file_extension: Optional[str] = None
                            if '.' in module:
                                file_extension = module.split('.')[1]
                                self.check_format(
                                    module, file_extension, verbose
                                )
                                self.check_path(module, verbose)
                                self.check_mode('w', verbose)
                                if self.is_file_ok():
                                    status = True
                            else:
                                file_extension = module
                                status = True
        return status
