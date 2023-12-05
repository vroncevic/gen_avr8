# -*- coding: UTF-8 -*-

'''
Module
    template_type.py
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
    Defines class TemplateType with attribute(s) and method(s).
    Creates API for checking project template type and template structure.
'''

import sys
from typing import Dict

try:
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
except ImportError as ats_error_message:
    # Force close python ATS ##################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, https://vroncevic.github.io/gen_avr8'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_avr8/blob/dev/LICENSE'
__version__ = '2.4.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TemplateType:
    '''
        Defines class TemplateType with attribute(s) and method(s).
        Creates API for checking project template type and template structure.

        It defines:

            :attributes:
                | GEN_VERBOSE - Console text indicator for process-phase.
                | APP_TEMPLATE - Application type of project.
                | LIB_TEMPLATE - Library type of project.
                | TEMPLATE_TYPE - Project template structures.
            :methods:
                | check_template_type - Check project template type.
                | setup_template_type - Setup template type (app | lib).
    '''

    GEN_VERBOSE: str = 'GEN_AVR8::PRO::TEMPLATE_TYPE'
    APP_TEMPLATE: str = 'app'
    LIB_TEMPLATE: str = 'lib'
    TEMPLATE_TYPE: Dict[str, str] = {
        APP_TEMPLATE: 'project_app.yaml',
        LIB_TEMPLATE: 'project_lib.yaml'
    }

    @classmethod
    def check_template_type(
        cls, template_type: str | None, verbose: bool = False
    ) -> bool:
        '''
            Check project template type (App | Lib).

            :param template_type: Project template type | None
            :type template_type: <str> | <NoneType>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: True (project type for ok) | False
            :rtype: <bool>
            :exceptions: ATSTypeError
        '''
        checker: ATSChecker = ATSChecker()
        error_msg: str | None = None
        error_id: int | None = None
        error_msg, error_id = checker.check_params([
            ('str:template_type', template_type)
        ])
        if error_id == checker.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        verbose_message(
            verbose,
            [f'{cls.GEN_VERBOSE} checking project type', template_type]
        )
        return template_type in cls.TEMPLATE_TYPE

    @classmethod
    def setup_template_type(
        cls, template_type: str | None, verbose: bool = False
    ) -> str | None:
        '''
            Setup template type (App | Lib).

            :param template_type: Project template type
            :type template_type: <str>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: Project type (app | lib) | None
            :rtype: <str> | <NoneType>
            :exceptions: ATSTypeError
        '''
        checker: ATSChecker = ATSChecker()
        error_msg: str | None = None
        error_id: int | None = None
        error_msg, error_id = checker.check_params([
            ('str:template_type', template_type)
        ])
        if error_id == checker.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        if template_type and cls.check_template_type(template_type, verbose):
            return cls.TEMPLATE_TYPE[template_type]
        return None
