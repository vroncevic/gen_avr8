# -*- coding: UTF-8 -*-

"""
 Module
     osc_selector.py
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
     Define class OSCSelector with attribute(s) and method(s).
"""

import sys

try:
    from pathlib import Path

    from ats_utilities.config.yaml.yaml2object import Yaml2Object
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.console_io.error import error_message
except ImportError as error:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2020, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"


class OSCSelector(object):
    """
        Define class OSCSelector with attribute(s) and method(s).
        Selecting FOSC for generating process of project structure.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                __CONF_DIR - Directory for configuration
                __FOSC_LIST - Configuration file with FOSC list
                __fosc_cfg - Yaml object for configuration
            method:
                __init__ - Initial constructor
                get_osc_cfg - Getter for OSC configuration object
                choose_osc - Selecting FOSC for target
    """

    __slots__ = ('VERBOSE', '__CONF_DIR', '__FOSC_LIST', '__fosc_cfg')
    VERBOSE = 'GEN_AVR8::AVR8_SETUP::OSC_SELECTOR'
    __CONF_DIR = '/../../conf/'
    __FOSC_LIST = 'fosc.yaml'

    def __init__(self, verbose=False):
        """
            Initial constructor.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(OSCSelector.VERBOSE, verbose, 'Initial form selector')
        current_dir = Path(__file__).parent
        template_dir = "{0}{1}".format(current_dir, OSCSelector.__CONF_DIR)
        mcu = "{0}{1}".format(template_dir, OSCSelector.__FOSC_LIST)
        self.__fosc_cfg = Yaml2Object(mcu)

    def get_osc_cfg(self):
        """
            Getter for OSC configuration object.
            :exceptions: None
        """
        return self.__fosc_cfg

    def choose_osc(self, verbose=False):
        """
            Selecting FOSC for target.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: FOSC | None
            :rtype: <str> | <NoneType>
            :exceptions: None
        """
        verbose_message(OSCSelector.VERBOSE, verbose, 'Selecting FOSC')
        fosc_cfg_list, fosc_name_index, fosc_name = None, -1, None
        fosc_cfg_list = self.__fosc_cfg.read_configuration(verbose=verbose)
        fosc_cfg_list = fosc_cfg_list['osc']
        fosc_cfg_list = fosc_cfg_list.split(' ')
        line = '#' * 30
        while True:
            print(line)
            for index in enumerate(fosc_cfg_list):
                print("\t{0}: {1}".format(index, fosc_cfg_list[index]))
            print(line)
            if sys.version_info > (3, 0):
                fosc_name_index = int(input(' Select FOSC: '))
            else:
                fosc_name_index = int(raw_input(' Select FOSC: '))
            if fosc_name_index not in enumerate(fosc_cfg_list):
                error_message(
                    OSCSelector.VERBOSE, 'Not an appropriate choice.'
                )
            else:
                fosc_name = fosc_cfg_list[fosc_name_index]
                print(line)
                break
        return fosc_name
