# -*- coding: UTF-8 -*-

'''
Module
    template_type.py
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
    Defines class TemplateType with attribute(s) and method(s).
    Creates an API for checking template type and template structure.
'''

import sys
from typing import Dict, List, Optional

try:
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_value_error import ATSValueError
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


class TemplateType:
    '''
        Defines class TemplateType with attribute(s) and method(s).
        Creates an API for checking template type and template structure.

        It defines:

            :attributes:
                | _GEN_VERBOSE - Console text indicator for process-phase.
                | _APP_TEMPLATE - Application type of project.
                | _LIB_TEMPLATE - Library type of project.
                | _TEMPLATE_TYPE - Project template structures.
            :methods:
                | check_template_type - Checks project template type.
                | setup_template_type - Sets template type (app | lib).
    '''

    _GEN_VERBOSE: str = 'GEN_AVR8::PRO::TEMPLATE_TYPE'
    _APP_TEMPLATE: str = 'app'
    _LIB_TEMPLATE: str = 'lib'
    _TEMPLATE_TYPE: Dict[str, str] = {
        _APP_TEMPLATE: 'project_app.yaml',
        _LIB_TEMPLATE: 'project_lib.yaml'
    }

    @classmethod
    def check_template_type(
        cls, template_type: Optional[str], verbose: bool = False
    ) -> bool:
        '''
            Checks project template type (App | Lib).

            :param template_type: Project template type | None
            :type template_type: <Optional[str]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: True (project type for ok) | False
            :rtype: <bool>
            :exceptions: ATSTypeError
        '''
        checker: ATSChecker = ATSChecker()
        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = checker.check_params([
            ('str:template_type', template_type)
        ])
        if error_id == checker.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        verbose_message(
            verbose,
            [f'{cls._GEN_VERBOSE.lower()} checking project ', template_type]
        )
        return template_type in cls._TEMPLATE_TYPE

    @classmethod
    def setup_template_type(
        cls, template_type: str, verbose: bool = False
    ) -> Optional[str]:
        '''
            Sets template type (App | Lib).

            :param template_type: Project template type
            :type template_type: <str>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: Project type (app | lib) | None
            :rtype: <Optional[str]>
            :exceptions: ATSTypeError | ATSValueError
        '''
        checker: ATSChecker = ATSChecker()
        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = checker.check_params([
            ('str:template_type', template_type)
        ])
        if error_id == checker.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        if not bool(template_type):
            raise ATSValueError('missing template type')
        if all([
            bool(template_type),
            cls.check_template_type(template_type, verbose)
        ]):
            return cls._TEMPLATE_TYPE[template_type]
        return None
