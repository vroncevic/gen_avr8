# -*- coding: UTF-8 -*-

'''
 Module
     module_type.py
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
     Defined class ModuleType with attribute(s) and method(s).
     Check module type (it can be source module | build module).
'''

import sys

try:
    from ats_utilities.console_io.verbose import verbose_message
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


class ModuleType:
    '''
        Defined class ModuleType with attribute(s) and method(s).
        Check module type (it can be source module | build module).
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
                | SOURCE - list of expected source extensions.
                | BUILD - list of expected build extensions/files.
            :methods:
                | pre_process_module - process module name.
                | is_source_module - check is source module.
                | is_build_module - check is build module.
                | __str__ - dunder method for ModuleType.
    '''

    GEN_VERBOSE = 'GEN_AVR8::PRO::MODULE_TYPE'
    SOURCE = ['.c', '.h']
    BUILD = ['.mk', 'Makefile']

    @classmethod
    def pre_process_module(cls, pro_type, pro_name, module, verbose=False):
        '''
            Process module name.

            :param pro_type: project type.
            :type pro_type: <str>
            :param pro_name: project name.
            :type pro_name: <str>
            :param module: module name.
            :type module: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: processed module name.
            :rtype: <str>
            :exceptions: None
        '''
        module_name = None
        if cls.is_source_module(module):
            if pro_type == 'lib':
                if cls.SOURCE[0] in module:
                    module_name = '{0}.c'.format(pro_name)
                if cls.SOURCE[1] in module:
                    module_name = '{0}.h'.format(pro_name)
            elif pro_type == 'app':
                module_name = module
        else:
            module_name = module
        verbose_message(cls.GEN_VERBOSE, verbose, 'module type', module)
        return module_name

    @classmethod
    def is_source_module(cls, module):
        '''
            Check is source module.

            :param module: module name.
            :type module: <str>
            :return: boolean status, True | False.
            :rtype: <bool>
            :exceptions: None
        '''
        source_type = False
        for source in cls.SOURCE:
            if source in module:
                source_type = True
        return source_type

    @classmethod
    def is_build_module(cls, module):
        '''
            Check is build module.

            :param module: module name.
            :type module: <str>
            :return: boolean status, True | False.
            :rtype: <bool>
            :exceptions: None
        '''
        build_type = False
        for build in cls.BUILD:
            if build in module:
                build_type = True
        return build_type

    def __str__(self):
        '''
            Dunder method for ModuleType.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ()'.format(self.__class__.__name__)
