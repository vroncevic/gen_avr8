# -*- coding: UTF-8 -*-

"""
 Module
     module_type.py
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
     Define class ModuleType with attribute(s) and method(s).
     Check module type (it can be source module | build module).
"""

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2021, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.4.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ModuleType(object):
    """
        Define class ModuleType with attribute(s) and method(s).
        Check module type (it can be source module | build module).
        It defines:

            :attributes:
                | __slots__ - Setting class slots.
                | __SOURCE - List of expected source extensions.
                | __BUILD - List of expected build extensions/files.
            :methods:
                | pre_process_module - Process module name.
                | is_source_module - Check is source module.
                | is_build_module - Check is build module.
    """

    __slots__ = ('__SOURCE', '__BUILD')
    __SOURCE = ['.c', '.h']
    __BUILD = ['.mk', 'Makefile']

    @classmethod
    def pre_process_module(cls, pro_type, pro_name, module):
        """
            Process module name.

            :param pro_type: Project type.
            :type pro_type: <str>
            :param pro_name: Project name.
            :type pro_name: <str>
            :param module: Module name.
            :type module: <str>
            :return: Processed module name.
            :rtype: <str>
            :exceptions: None
        """
        module_name = None
        if cls.is_source_module(module):
            if pro_type == 'lib':
                if cls.__SOURCE[0] in module:
                    module_name = "{0}.c".format(pro_name)
                if cls.__SOURCE[1] in module:
                    module_name = "{0}.h".format(pro_name)
            elif pro_type == 'app':
                module_name = module
        else:
            module_name = module
        return module_name

    @classmethod
    def is_source_module(cls, module):
        """
            Check is source module.

            :param module: Module name.
            :type module: <str>
            :return: True | False.
            :rtype: <bool>
            :exceptions: None
        """
        source_type = False
        for source in cls.__SOURCE:
            if source in module:
                source_type = True
        return source_type

    @classmethod
    def is_build_module(cls, module):
        """
            Check is build module.

            :param module: Module name.
            :type module: <str>
            :return: True | False.
            :rtype: <bool>
            :exceptions: None
        """
        build_type = False
        for build in cls.__BUILD:
            if build in module:
                build_type = True
        return build_type
