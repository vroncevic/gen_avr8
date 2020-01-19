# -*- coding: UTF-8 -*-
# mcu_selector.py
# Copyright (C) 2020 Vladimir Roncevic <elektron.ronca@gmail.com>
#
# gen_avr8 is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# gen_avr8 is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.
#

import sys

try:
    from pathlib import Path

    from ats_utilities.config.yaml.yaml2object import Yaml2Object
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.console_io.error import error_message
except ImportError as e:
    msg = "\n{0}\n{1}\n".format(__file__, e)
    sys.exit(msg)  # Force close python ATS ##################################

__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2020, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"


class MCUSelector(object):
    """
        Define class MCUSelector with attribute(s) and method(s).
        Selecting MCU target for generating process of project structure.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                __CONF_DIR - Directory for configuration
                __MCU_LIST - Configuration file with MCU list
                __mcu_cfg - Yaml object for configuration
            method:
                __init__ - Initial constructor
                choose_mcu - Selecting MCU target
    """

    __slots__ = ('VERBOSE', '__CONF_DIR', '__MCU_LIST', '__mcu_cfg')
    VERBOSE = 'GEN_AVR8::AVR8_SETUP::MCU_SELECTOR'
    __CONF_DIR = '/../../conf/'
    __MCU_LIST = 'mcu.yaml'

    def __init__(self, verbose=False):
        """
            Initial constructor.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(MCUSelector.VERBOSE, verbose, 'Initial MCU selector')
        current_dir = Path(__file__).parent
        template_dir = "{0}{1}".format(current_dir, MCUSelector.__CONF_DIR)
        mcu = "{0}{1}".format(template_dir, MCUSelector.__MCU_LIST)
        self.__mcu_cfg = Yaml2Object(mcu)

    def choose_mcu(self, verbose=False):
        """
            Selecting MCU target.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: MCU name | None
            :rtype: <str> | <NoneType>
            :exceptions: None
        """
        verbose_message(MCUSelector.VERBOSE, verbose, 'Selecting MCU')
        mcu_cfg_list, mcu_name_index, mcu_name = None, -1, None
        mcu_cfg_list = self.__mcu_cfg.read_configuration(verbose=verbose)
        mcu_cfg_list = mcu_cfg_list['mcu']
        mcu_cfg_list = mcu_cfg_list.split(' ')
        while True:
            print('\n')
            for index in range(len(mcu_cfg_list)):
                print("\t{0}: {1}".format(index, mcu_cfg_list[index]))
            print('\n')
            mcu_name_index = int(raw_input(' Select MCU: '))
            if mcu_name_index not in range(len(mcu_cfg_list)):
                error_message(
                    MCUSelector.VERBOSE, 'Not an appropriate choice.'
                )
            else:
                mcu_name = mcu_cfg_list[mcu_name_index]
                break
        return mcu_name

