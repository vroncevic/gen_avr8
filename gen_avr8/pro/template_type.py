# -*- coding: UTF-8 -*-

'''
 Module
     template_type.py
 Copyright
     Copyright (C) 2021 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Define class TemplateType with method(s).
     Check project template type and template structure.
'''

import sys

try:
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2021, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.4.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TemplateType(object):
    '''
        Define class TemplateType with method(s).
        Check project template type and template structure.
        It defines:

            :attributes:
                | __slots__ - Setting class slots.
                | VERBOSE - Console text indicator for current process-phase.
                | TEMPLATE_TYPE - Project template structures.
            :methods:
                | check_template_type - Check project template type.
                | setup_template_type - Setup template type (app | lib).
    '''

    __slots__ = ('VERBOSE', 'TEMPLATE_TYPE', 'APP_TEMPLATE', 'LIB_TEMPLATE')
    VERBOSE = 'GEN_AVR8::PRO::TEMPLATE_TYPE'
    APP_TEMPLATE, LIB_TEMPLATE = 'app', 'lib'
    TEMPLATE_TYPE = {
        APP_TEMPLATE: 'project_app.yaml',
        LIB_TEMPLATE: 'project_lib.yaml'
    }

    @classmethod
    def check_template_type(cls, template_type, verbose=False):
        '''
            Check project template type (App | Lib).

            :param template_type: Project Template type.
            :type template_type: <str>
            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :return: True project type ok else False.
            :rtype: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params(
            [('str:template_type', template_type)]
        )
        if status == ATSChecker.TYPE_ERROR: raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR: raise ATSBadCallError(error)
        verbose_message(
            TemplateType.VERBOSE, verbose,
            'checking project type', template_type
        )
        return bool(
            template_type in TemplateType.TEMPLATE_TYPE.keys()
        )

    @classmethod
    def setup_template_type(cls, template_type, verbose=False):
        '''
            Setup template type (App | Lib).

            :param template_type: Project Template type.
            :type template_type: <str>
            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :return: Project type (app | lib) | None.
            :rtype: <str> | <NoneType>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params(
            [('str:template_type', template_type)]
        )
        if status == ATSChecker.TYPE_ERROR: raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR: raise ATSBadCallError(error)
        if cls.check_template_type(template_type, verbose=verbose):
            return TemplateType.TEMPLATE_TYPE[template_type]
        return None
