# -*- coding: UTF-8 -*-

"""
 Module
     avr8_setup.py
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
from inspect import stack

try:
    from avr8_pro.mcu_selector import MCUSelector
    from avr8_pro.osc_selector import OSCSelector
    from avr8_pro.read_template import ReadTemplate
    from avr8_pro.write_template import WriteTemplate

    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as error:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2019, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class AVR8Setup(object):
    """
        Define class AVR8Setup with attribute(s) and method(s).
        Generate AVR project skeleton.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                __mcu_sel - MCU selector API
                __fosc_sel - FOSC selector API
                __reader - Reader API
                __writer - Writer API
            method:
                __init__ - Initial constructor
                get_mcu_selector - Getter for MCU selector
                get_fosc_selector - Getter for FOSC selector
                get_reader - Getter for reader object
                get_writer - Getter for writer object
                gen_pro_setup - Generate project skeleton
    """

    __slots__ = ('VERBOSE', '__mcu_sel', '__fosc_sel', '__reader', '__writer')
    VERBOSE = 'GEN_AVR8::AVR8_SETUP::AVR8SETUP'

    def __init__(self, verbose=False):
        """
            Initial constructor
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(AVR8Setup.VERBOSE, verbose, 'Initial setup')
        self.__mcu_sel = MCUSelector(verbose=verbose)
        self.__fosc_sel = OSCSelector(verbose=verbose)
        self.__reader = ReadTemplate(verbose=verbose)
        self.__writer = WriteTemplate(verbose=verbose)

    def get_mcu_selector(self):
        """
            Getter for MCU selector.
            :exceptions: None
        """
        return self.__mcu_sel

    def get_fosc_selector(self):
        """
            Getter for FOSC selector.
            :exceptions: None
        """
        return self.__fosc_sel

    def get_reader(self):
        """
            Getter for reader object.
            :exceptions: None
        """
        return self.__reader

    def get_writer(self):
        """
            Getter for writer object.
            :exceptions: None
        """
        return self.__writer

    def gen_pro_setup(self, project_name, verbose=False):
        """
            Generate setup.py for python package.
            :param project_name: Project name
            :type project_name: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: True (success) | False
            :rtype: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        func, status, project_data = stack()[0][3], False, {}
        project_txt = 'Argument: expected project_name <str> object'
        project_msg = "{0} {1} {2}".format('def', func, project_txt)
        if project_name is None or not project_name:
            raise ATSBadCallError(project_msg)
        if not isinstance(project_name, str):
            raise ATSTypeError(project_msg)
        verbose_message(
            AVR8Setup.VERBOSE, verbose, 'Generating project', project_name
        )
        project_data['templates'] = self.__reader.read(verbose=verbose)
        project_data['name'] = project_name
        mcu = self.__mcu_sel.choose_mcu(verbose=verbose)
        project_data['mcu'] = mcu
        fosc = self.__fosc_sel.choose_osc(verbose=verbose)
        project_data['osc'] = fosc
        if bool(project_data):
            status = self.__writer.write(project_data, verbose=verbose)
        return True if status else False
