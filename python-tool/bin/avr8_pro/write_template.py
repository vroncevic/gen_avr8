# -*- coding: UTF-8 -*-

"""
 Module
     write_template.py
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
     Define class WriteTemplate with attribute(s) and method(s).
     Write template content with parameters to a project setup.
"""

import sys
from inspect import stack
from os import getcwd, chmod, mkdir
from os.path import exists
from string import Template

try:
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as error:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2020, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class WriteTemplate(object):
    """
        Define class WriteTemplate with attribute(s) and method(s).
        Write template content with parameters to a project setup.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                __project_status - Project status
            method:
                __init__ - Initial constructor
                get_project_status - Getter for project status object
                write - Write a template content to a project setup
    """

    __slots__ = ('VERBOSE', '__project_status')
    VERBOSE = 'GEN_AVR8::AVR8_PRO::WRITE_TEMPLATE'

    def __init__(self, verbose=False):
        """
            Initial constructor
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(WriteTemplate.VERBOSE, verbose, 'Initial writer')
        self.__project_status = False

    def get_project_status(self):
        """
            Getter for project status object.
            :return: Ptoject status
            :rtype: <bool>
            :exceptions: None
        """
        return self.__project_status

    def write(self, project_data, verbose=False):
        """
            Write setup content to file.
            :param project_data: Project data
            :type project_data: <dict>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: True (success) | False
            :rtype: <bool>
            :exception: ATSBadCallError | ATSTypeError
        """
        status, template, module = False, None, None
        func, current_dir = stack()[0][3], getcwd()
        setup_txt = 'First argument: expected project_data <dict> object'
        setup_msg = "{0} {1} {2}".format('def', func, setup_txt)
        if project_data is None or not project_data:
            raise ATSBadCallError(setup_msg)
        if not isinstance(project_data, dict):
            raise ATSTypeError(setup_msg)
        project_content = project_data['templates']
        build_dir = "{0}/{1}".format(current_dir, 'build')
        self.__project_status = all(
            [
                bool(project_content), bool(project_data['name']),
                bool(project_data['mcu']), bool(project_data['osc'])
            ]
        )
        if self.__project_status:
            for pro_item in project_content.keys():
                if '.c' in project_content[pro_item][0]:
                    module = "{0}/{1}".format(
                        current_dir, project_content[pro_item][0]
                    )
                else:
                    module = "{0}/{1}".format(
                        build_dir, project_content[pro_item][0]
                    )
                verbose_message(
                    WriteTemplate.VERBOSE, verbose,
                    'Write project module file', module
                )
                project = {
                    'PRO': "{0}".format(project_data['name']),
                    'MCU': "{0}".format(project_data['mcu']),
                    'OSC': "{0}".format(project_data['osc'])
                }
                template = Template(project_content[pro_item][1])
                if template:
                    if not exists(build_dir):
                        mkdir(build_dir)
                    with open(module, 'w') as module_file:
                        if bool(module_file):
                            module_file.write(template.substitute(project))
                            chmod(module, 0o666)
                            status = True
        return True if status else False
