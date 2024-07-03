# -*- coding: UTF-8 -*-

'''
Module
    __init__.py
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
    Defines class AVR8Setup with attribute(s) and method(s).
    Generates AVR project skeleton.
'''

import sys
from typing import Any, Dict, List, Optional

try:
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config_io.yaml.yaml2object import Yaml2Object
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from gen_avr8.pro.module_type import ModuleType
    from gen_avr8.pro.mcu_selector import MCUSelector
    from gen_avr8.pro.osc_selector import OSCSelector
    from gen_avr8.pro.template_dir import TemplateDir
    from gen_avr8.pro.template_type import TemplateType
    from gen_avr8.pro.read_template import ReadTemplate
    from gen_avr8.pro.write_template import WriteTemplate
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


class AVR8Setup(ATSChecker):
    '''
        Defines class AVR8Setup with attribute(s) and method(s).
        Generates AVR project skeleton.

        It defines:

            :attributes:
                | _GEN_VERBOSE - Console text indicator for process-phase.
                | _mcu_sel - MCU selector API.
                | _fosc_sel - FOSC selector API.
                | _reader - Reader API.
                | _writer - Writer API.
                | _setup - Project setup.
            :methods:
                | __init__ - Initials AVR8Setup constructor.
                | project_setup - Property methods for set operations.
                | gen_pro_setup - Generates project skeleton.
    '''

    _GEN_VERBOSE: str = 'GEN_AVR8::PRO::AVR8SETUP'

    def __init__(self, verbose: bool = False) -> None:
        '''
            Initials AVR8Setup constructor.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        super().__init__()
        verbose_message(verbose, [f'{self._GEN_VERBOSE.lower()} init setup'])
        self._mcu_sel = MCUSelector(verbose)
        self._fosc_sel = OSCSelector(verbose)
        self._reader = ReadTemplate(verbose)
        self._writer = WriteTemplate(verbose)
        self._setup: Dict[Any, Any] = {}

    def project_setup(
        self,
        project_name: Optional[str],
        project_type: Optional[str],
        verbose: bool = False
    ) -> None:
        '''
            Property methods for set operations.

            :param project_name: Project name | None
            :type project_name: <Optional[str]>
            :param project_type: Project type | None
            :type project_type: <Optional[str]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError
        '''
        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = self.check_params([
            ('str:project_name', project_name),
            ('str:project_type', project_type)
        ])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        verbose_message(
            verbose,
            [f'{self._GEN_VERBOSE.lower()} set {project_name} {project_type}']
        )
        self._setup.update({'name': project_name})
        self._setup.update({'type': project_type})

    def gen_pro_setup(self, verbose: bool = False) -> bool:
        '''
            Generates AVR8 project setup.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: True (success operation) | False
            :rtype: <bool>
            :exceptions: None
        '''
        status: bool = False
        if any(['name' not in self._setup, 'type' not in self._setup]):
            return status
        if any([
            not bool(self._setup['name']), not bool(self._setup['type'])
        ]):
            return status
        verbose_message(
            verbose, [
                f'{self._GEN_VERBOSE.lower()} gen project',
                self._setup['type'], self._setup['name']
            ]
        )
        conf_dir: Optional[str] = TemplateDir.setup_conf_dir(verbose)
        if not bool(conf_dir):
            return status
        setup_template: Optional[str] = TemplateType.setup_template_type(
            self._setup['type'], verbose
        )
        if not bool(setup_template):
            return status
        yml2obj: Yaml2Object = Yaml2Object(f'{conf_dir}{setup_template}')
        all_stat: List[bool] = []
        if bool(yml2obj):
            pro_cfg: Dict[str, str] | None = yml2obj.read_configuration()
            pro_data: Dict[Any, Any] = {}
            if bool(pro_cfg):
                templates: List[str] | None = pro_cfg['templates'].split(' ')
                modules: List[str] | None = pro_cfg['modules'].split(' ')
                if any([not bool(templates), not bool(modules)]):
                    return status
                pro_data['name'] = self._setup['name']
                pro_data['type'] = self._setup['type']
                pro_data['mcu'] = self._mcu_sel.choose_mcu(verbose)
                pro_data['osc'] = self._fosc_sel.choose_osc(verbose)
                if any([not bool(pro_data['mcu']), not bool(pro_data['osc'])]):
                    return status
                self._writer.pro_dir = self._setup['name']
                for template, module in zip(templates, modules):
                    template_dir: Optional[
                        str
                    ] = TemplateDir.setup_template_dir(verbose)
                    pro_data['template'] = self._reader.read(
                        f'{template_dir}{self._setup["type"]}/{template}',
                        verbose
                    )
                    pro_data['module'] = ModuleType.pre_process_module(
                        self._setup['type'],
                        self._setup['name'],
                        module, verbose
                    )
                    all_stat.append(self._writer.write(pro_data, verbose))
                if all(all_stat) and len(templates) == len(all_stat):
                    status = True
        return status
