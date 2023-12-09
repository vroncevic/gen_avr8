# -*- coding: UTF-8 -*-

'''
Module
    __init__.py
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
    Defines class AVR8Setup with attribute(s) and method(s).
    Generates AVR project skeleton.
'''

import sys
from typing import Any, Dict, List

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
__copyright__ = 'Copyright 2018, https://vroncevic.github.io/gen_avr8'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_avr8/blob/dev/LICENSE'
__version__ = '2.5.5'
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
                | _pro_setup - Project setup.
            :methods:
                | __init__ - Initial AVR8Setup constructor.
                | project_setup - Property methods for set operations.
                | gen_pro_setup - Generate project skeleton.
    '''

    _GEN_VERBOSE: str = 'GEN_AVR8::PRO::AVR8SETUP'

    def __init__(self, verbose: bool = False) -> None:
        '''
            Initial AVR8Setup constructor.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        super().__init__()
        verbose_message(verbose, [f'{self._GEN_VERBOSE} init setup'])
        self._mcu_sel = MCUSelector(verbose)
        self._fosc_sel = OSCSelector(verbose)
        self._reader = ReadTemplate(verbose)
        self._writer = WriteTemplate(verbose)
        self._pro_setup: Dict[Any, Any] = {}

    def project_setup(
        self,
        project_name: str | None,
        project_type: str | None,
        verbose: bool = False
    ) -> None:
        '''
            Setter for project setup.

            :param project_name: Project name | None
            :type project_name: <str> | <NoneType>
            :param project_type: Project type | None
            :type project_type: <str> | <NoneType>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError
        '''
        error_msg: str | None = None
        error_id: int | None = None
        error_msg, error_id = self.check_params([
            ('str:project_name', project_name),
            ('str:project_type', project_type)
        ])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        verbose_message(
            verbose,
            [f'{self._GEN_VERBOSE} setup {project_name} {project_type}']
        )
        self._pro_setup.update({'name': project_name})
        self._pro_setup.update({'type': project_type})

    def gen_pro_setup(self, verbose: bool = False) -> bool:
        '''
            Generate AVR8 project setup.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: True (success operation) | False
            :rtype: <bool>
            :exceptions: None
        '''
        status: bool = False
        if 'name' not in self._pro_setup or 'type' not in self._pro_setup:
            return status
        if not self._pro_setup['name'] or not self._pro_setup['type']:
            return status
        verbose_message(
            verbose, [
                f'{self._GEN_VERBOSE} gen project',
                self._pro_setup['type'],
                self._pro_setup['name']
            ]
        )
        conf_dir: str | None = TemplateDir.setup_conf_dir(verbose)
        if not conf_dir:
            return status
        setup_template: str | None = TemplateType.setup_template_type(
            self._pro_setup['type'], verbose
        )
        if not setup_template:
            return status
        yml2obj: Yaml2Object = Yaml2Object(f'{conf_dir}{setup_template}')
        all_stat: List[bool] = []
        if yml2obj:
            pro_cfg: Dict[str, str] | None = yml2obj.read_configuration()
            pro_data: Dict[Any, Any] = {}
            if pro_cfg:
                templates: List[str] | None = pro_cfg['templates'].split(' ')
                modules: List[str] | None = pro_cfg['modules'].split(' ')
                if not templates or not modules:
                    return status
                pro_data['name'] = self._pro_setup['name']
                pro_data['type'] = self._pro_setup['type']
                pro_data['mcu'] = self._mcu_sel.choose_mcu(verbose)
                pro_data['osc'] = self._fosc_sel.choose_osc(verbose)
                if not pro_data['mcu'] or not pro_data['osc']:
                    return status
                self._writer.pro_dir = self._pro_setup['name']
                for template, module in zip(templates, modules):
                    template_dir: str | None = TemplateDir.setup_template_dir(
                        verbose
                    )
                    pro_data['template'] = self._reader.read(
                        f'{template_dir}{self._pro_setup["type"]}/{template}',
                        verbose
                    )
                    pro_data['module'] = ModuleType.pre_process_module(
                        self._pro_setup['type'],
                        self._pro_setup['name'],
                        module, verbose
                    )
                    all_stat.append(self._writer.write(pro_data, verbose))
                if all(all_stat) and len(templates) == len(all_stat):
                    status = True
        return status
