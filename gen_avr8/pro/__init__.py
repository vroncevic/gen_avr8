# -*- coding: UTF-8 -*-

"""
 Module
     __init__.py
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
     Define class AVR8Setup with attribute(s) and method(s).
     Generate AVR project skeleton.
"""

import sys

try:
    from ats_utilities.checker import ATSChecker
    from gen_avr8.pro.module_type import ModuleType
    from gen_avr8.pro.mcu_selector import MCUSelector
    from gen_avr8.pro.osc_selector import OSCSelector
    from gen_avr8.pro.template_dir import TemplateDir
    from gen_avr8.pro.template_type import TemplateType
    from gen_avr8.pro.read_template import ReadTemplate
    from gen_avr8.pro.write_template import WriteTemplate
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config_io.yaml.yaml2object import Yaml2Object
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as error_message:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2019, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.4.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class AVR8Setup(object):
    """
        Define class AVR8Setup with attribute(s) and method(s).
        Generate AVR project skeleton.
        It defines:

            :attributes:
                | __slots__ - Setting class slots.
                | VERBOSE - Console text indicator for current process-phase.
                | __mcu_sel - MCU selector API.
                | __fosc_sel - FOSC selector API.
                | __reader - Reader API.
                | __writer - Writer API.
                | __project_setup - Project setup.
            :methods:
                | __init__ - Initial constructor.
                | project_setup - Property methods for set/get operations.
                | gen_pro_setup - Generate project skeleton.
    """

    __slots__ = (
        'VERBOSE',
        '__mcu_sel',
        '__fosc_sel',
        '__reader',
        '__writer',
        '__project_setup'
    )
    VERBOSE = 'GEN_AVR8::PRO::AVR8SETUP'

    def __init__(self, verbose=False):
        """
            Initial constructor.

            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(AVR8Setup.VERBOSE, verbose, 'init setup')
        self.__mcu_sel = MCUSelector(verbose=verbose)
        self.__fosc_sel = OSCSelector(verbose=verbose)
        self.__reader = ReadTemplate(verbose=verbose)
        self.__writer = WriteTemplate(verbose=verbose)
        self.__project_setup = None

    @property
    def project_setup(self):
        """
            Getter for writer object.

            :return: Write template object | None.
            :rtype: <WriteTemplate> | <NoneType>
            :exceptions: None
        """
        return self.__project_setup

    @project_setup.setter
    def project_setup(self, project_setup):
        """
            Setter for project setup.

            :param project_setup: Project setup.
            :type project_setup: <dict>
            :exceptions: ATSTypeError | ATSBadCallError
        """
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params(
            [('dict:project_setup', project_setup)]
        )
        if status == ATSChecker.TYPE_ERROR: raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR: raise ATSBadCallError(error)
        self.__project_setup = project_setup

    def gen_pro_setup(self, verbose=False):
        """
            Generate AVR8 project setup.

            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :return: True (success) | False.
            :rtype: <bool>
            :exceptions: None
        """
        verbose_message(
            AVR8Setup.VERBOSE, verbose, 'generate project',
            self.__project_setup['type'], self.__project_setup['name']
        )
        yml2obj, status, statuses = Yaml2Object(
            "{0}{1}".format(
                TemplateDir.setup_conf_dir(verbose),
                TemplateType.setup_template_type(
                    self.__project_setup['type'], verbose
                )
            )
        ), False, []
        if bool(yml2obj):
            pro_cfg, project_data = yml2obj.read_configuration(), {}
            templates = pro_cfg['templates'].split(' ')
            modules = pro_cfg['modules'].split(' ')
            project_data['name'] = self.__project_setup['name']
            project_data['type'] = self.__project_setup['type']
            project_data['mcu'] = self.__mcu_sel.choose_mcu(verbose=verbose)
            project_data['osc'] = self.__fosc_sel.choose_osc(verbose=verbose)
            self.__writer.pro_dir = self.__project_setup['name']
            for template, module in zip(templates, modules):
                project_data['template'] = self.__reader.read(
                    template_file="{0}{1}/{2}".format(
                    TemplateDir.setup_template_dir(verbose),
                    self.__project_setup['type'], template
                    ), verbose=verbose
                )
                project_data['module'] = ModuleType.pre_process_module(
                    self.__project_setup['type'],
                    self.__project_setup['name'],
                    module
                )
                statuses.append(
                    self.__writer.write(project_data, verbose=verbose)
                )
            if all(statuses) and len(templates) == len(statuses):
                status = True
        return True if status else False