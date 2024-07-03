# -*- coding: UTF-8 -*-

'''
Module
    module_type.py
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
    Defines class ModuleType with attribute(s) and method(s).
    Checks module type (it can be source module | build module).
'''

import sys
from typing import List, Optional

try:
    from ats_utilities.console_io.verbose import verbose_message
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


class ModuleType:
    '''
        Defines class ModuleType with attribute(s) and method(s).
        Checks module type (it can be source module | build module).

        It defines:

            :attributes:
                | _GEN_VERBOSE - Console text indicator for process-phase.
                | _SOURCE - List of expected source extensions.
                | _BUILD - List of expected build extensions/files.
            :methods:
                | pre_process_module - Processes module name.
                | is_source_module - Checks is source module.
                | is_build_module - Checks is build module.
    '''

    _GEN_VERBOSE: str = 'GEN_AVR8::PRO::MODULE_TYPE'
    _SOURCE: List[str] = ['.c', '.h']
    _BUILD: List[str] = ['.mk', 'Makefile']

    @classmethod
    def pre_process_module(
        cls,
        pro_type: Optional[str],
        pro_name: Optional[str],
        module: Optional[str],
        verbose: bool = False
    ) -> Optional[str]:
        '''
            Processes module name.

            :param pro_type: Project type | None
            :type pro_type: <Optional[str]>
            :param pro_name: Project name | None
            :type pro_name: <Optional[str]>
            :param module: Module name | None
            :type module: <Optional[str]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: Processed module name | None
            :rtype: <Optional[str]>
            :exceptions: None
        '''
        module_name: Optional[str] = None
        if bool(module) and cls.is_source_module(module):
            if pro_type == 'lib':
                if module.endswith(cls._SOURCE[0]):
                    module_name = f'{pro_name}.c'
                if module.endswith(cls._SOURCE[1]):
                    module_name = f'{pro_name}.h'
            elif pro_type == 'app':
                module_name = module
        elif bool(module) and cls.is_build_module(module):
            module_name = module
        verbose_message(
            verbose, [f'{cls._GEN_VERBOSE.lower()} module type', module]
        )
        return module_name

    @classmethod
    def is_source_module(cls, module: Optional[str]) -> bool:
        '''
            Checks is source module.

            :param module: module name | None
            :type module: <Optional[str]>
            :return: True (module is source type) | False
            :rtype: <bool>
            :exceptions: None
        '''
        source_type_supported: bool = False
        if bool(module):
            for source_type_ext in cls._SOURCE:
                if module.endswith(source_type_ext):
                    source_type_supported = True
        return source_type_supported

    @classmethod
    def is_build_module(cls, module: Optional[str]) -> bool:
        '''
            Checks is build module.

            :param module: Module name | None
            :type module: <Optional[str]>
            :return: True (module is build type) | False
            :rtype: <bool>
            :exceptions: None
        '''
        build_type_supported = False
        if bool(module):
            for build_type_ext in cls._BUILD:
                if module.endswith(build_type_ext):
                    build_type_supported = True
        return build_type_supported
