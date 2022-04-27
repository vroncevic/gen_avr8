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
     Defined class TemplateType with attribute(s) and method(s).
     Created API for checking project template type and template structure.
'''

import sys

try:
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
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


class TemplateType:
    '''
        Defined class TemplateType with attribute(s) and method(s).
        Created API for checking project template type and template structure.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
                | APP_TEMPLATE - application type of project.
                | LIB_TEMPLATE - library type of project.
                | TEMPLATE_TYPE - project template structures.
            :methods:
                | check_template_type - check project template type.
                | setup_template_type - setup template type (app | lib).
                | __str__ - dunder method for TemplateType.
    '''

    GEN_VERBOSE = 'GEN_AVR8::PRO::TEMPLATE_TYPE'
    APP_TEMPLATE, LIB_TEMPLATE = 'app', 'lib'
    TEMPLATE_TYPE = {
        APP_TEMPLATE: 'project_app.yaml',
        LIB_TEMPLATE: 'project_lib.yaml'
    }

    @classmethod
    def check_template_type(cls, template_type, verbose=False):
        '''
            Check project template type (App | Lib).

            :param template_type: project template type.
            :type template_type: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: boolean status, True project type for ok | False.
            :rtype: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('str:template_type', template_type)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        verbose_message(
            TemplateType.GEN_VERBOSE, verbose,
            'checking project type', template_type
        )
        return bool(template_type in TemplateType.TEMPLATE_TYPE.keys())

    @classmethod
    def setup_template_type(cls, template_type, verbose=False):
        '''
            Setup template type (App | Lib).

            :param template_type: project template type.
            :type template_type: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: project type (app | lib) | None.
            :rtype: <str> | <NoneType>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('str:template_type', template_type)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        if cls.check_template_type(template_type, verbose=verbose):
            return TemplateType.TEMPLATE_TYPE[template_type]
        return None

    def __str__(self):
        '''
            Dunder method for TemplateType.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ()'.format(self.__class__.__name__)
