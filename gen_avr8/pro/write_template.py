# -*- coding: UTF-8 -*-

'''
 Module
     write_template.py
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
     Define class WriteTemplate with attribute(s) and method(s).
     Write template content with parameters to a project module.
'''

import sys
from os import getcwd, chmod, mkdir
from string import Template

try:
    from gen_avr8.pro.module_type import ModuleType
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
__license__ = 'https://github.com/vroncevic/gen_avr8/blob/master/LICENSE'
__version__ = '1.5.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class WriteTemplate(object):
    '''
        Define class WriteTemplate with attribute(s) and method(s).
        Write template content with parameters to a project module.
        It defines:

            :attributes:
                | __slots__ - Setting class slots.
                | VERBOSE - Console text indicator for current process-phase.
                | __pro_dir - Current project directory.
            :methods:
                | __init__ - Initial constructor.
                | pro_dir - Property methods for set/get operations.
                | check_module - Check project module.
                | write - Write a template content to a project module.
                | __str__ - Dunder method for WriteTemplate.
    '''

    __slots__ = ('VERBOSE', '__pro_dir')
    VERBOSE = 'GEN_AVR8::PRO::WRITE_TEMPLATE'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        verbose_message(WriteTemplate.VERBOSE, verbose, 'init writer')
        self.__pro_dir = None

    @property
    def pro_dir(self):
        '''
            Property method for getting project dir.

            :return: Project dir | None.
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        return self.__pro_dir

    @pro_dir.setter
    def pro_dir(self, pro_dir):
        '''
            Property method for setting/creating project dir.

            :param pro_dir: Project dir.
            :type pro_dir: <str>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params(
            [('str:pro_dir', pro_dir)]
        )
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        self.__pro_dir = '{0}/{1}'.format(getcwd(), pro_dir)
        mkdir(self.__pro_dir)
        mkdir('{0}/{1}'.format(self.__pro_dir, 'build'))

    def check_module(self, module, verbose=False):
        '''
            Check project module.

            :param module: Module name.
            :type module: <str>
            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :return: 'build' | 'source'| None (wrong module name).
            :rtype: <str> | <NoneType>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params(
            [('str:module', module)]
        )
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        is_source, is_build, module_type = False, False, None
        is_source = ModuleType.is_source_module(module)
        is_build = ModuleType.is_build_module(module)
        if is_source and not is_build:
            module_type = 'source'
        if not is_source and is_build:
            module_type = 'build'
        verbose_message(
            WriteTemplate.VERBOSE, verbose, 'module type', module_type
        )
        return module_type

    def write(self, project_data, verbose=False):
        '''
            Write a template content to a project module.

            :param project_data: Project data.
            :type project_data: <dict>
            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :return: True (success) | False.
            :rtype: <bool>
            :exception: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params(
            [('dict:project_data', project_data)]
        )
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        status = False
        module_type = self.check_module(project_data['module'])
        if bool(module_type):
            project = {
                'PRO': '{0}'.format(project_data['name']),
                'MCU': '{0}'.format(project_data['mcu']),
                'OSC': '{0}'.format(project_data['osc'])
            }
            template = Template(project_data['template'])
            if template:
                module = None
                if module_type == 'source':
                    module = '{0}/{1}'.format(
                        self.__pro_dir, project_data['module']
                    )
                if module_type == 'build':
                    module = '{0}/{1}/{2}'.format(
                        self.__pro_dir, 'build', project_data['module']
                    )
                if module:
                    with open(module, 'w') as module_file:
                        if bool(module_file):
                            verbose_message(
                                WriteTemplate.VERBOSE, verbose,
                                'write project module file', module
                            )
                            module_file.write(template.substitute(project))
                            chmod(module, 0o666)
                            status = True
        return True if status else False

    def __str__(self):
        '''
            Dunder method for WriteTemplate.

            :return: Object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1})'.format(
            self.__class__.__name__, self.__pro_dir
        )
