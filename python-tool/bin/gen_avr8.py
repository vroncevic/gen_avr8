# -*- coding: utf-8 -*-

"""
 Module
     gen_avr8.py
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
     Define class GenAVR8 with attribute(s) and method(s).
     Load a settings, create an interface and run operation(s).
"""

import sys
from os import getcwd

try:
    from pathlib import Path

    from avr8_pro.avr8_setup import AVR8Setup

    from ats_utilities.cfg_base import CfgBase
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.console_io.success import success_message
    from ats_utilities.config.yaml.yaml2object import Yaml2Object
except ImportError as error:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2019, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.1.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"


class GenAVR8(CfgBase):
    """
        Define class GenAVR8 with attribute(s) and method(s).
        Load a settings, create an interface and run operation(s).
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                __CONFIG - Configuration file path
                __OPS - Tool options (list)
            method:
                __init__ - Initial constructor
                process - Process and run tool option
    """

    __slots__ = ('VERBOSE', '__CONFIG', '__OPS')
    VERBOSE = 'GEN_AVR8'
    __CONFIG = '/../conf/gen_avr8.cfg'
    __OPS = ['-g', '--gen', '-c', '--conf', '-h', '--version']

    def __init__(self, verbose=False):
        """
            Loading configuration and setting argument options.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(GenAVR8.VERBOSE, verbose, 'Initial configuration')
        tool_dir = Path(__file__).resolve().parent
        base_config_file = "{0}{1}".format(tool_dir, GenAVR8.__CONFIG)
        CfgBase.__init__(self, base_config_file, verbose=verbose)
        if self.tool_status:
            self.add_new_option(
                GenAVR8.__OPS[0], GenAVR8.__OPS[1], dest="pro",
                help="generate AVR8 project skeleton"
            )
            self.add_new_option(
                GenAVR8.__OPS[2], GenAVR8.__OPS[3], dest="conf",
                help="load parameters from yaml file"
            )

    def process(self, verbose=False):
        """
            Process and run operation.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: True (success) | False
            :rtype: <bool>
            :exceptions: None
        """
        status = False
        if self.tool_status:
            self.show_base_info(verbose=verbose)
            if len(sys.argv) > 1:
                operation = sys.argv[1]
                if operation not in GenAVR8.__OPS:
                    sys.argv = []
                    sys.argv.append("-h")
            else:
                sys.argv.append("-h")
            current_dir, pro_setup = getcwd(), {}
            opts, script = self.parse_args(sys.argv)
            if len(script) == 1 and bool(opts.pro):
                pro_setup['name'] = opts.pro
                if bool(opts.conf):
                    project_setup_path = "{0}/{1}".format(
                        current_dir, "{0}".format(opts.conf)
                    )
                    cfg = Yaml2Object(project_setup_path, verbose=verbose)
                    pro_setup['conf'] = cfg.read_configuration(verbose=verbose)
                else:
                    pro_setup['conf'] = None
                check_pro_cfg = any(
                    [
                        all([bool(opts.conf), bool(pro_setup['conf'])]),
                        all([not bool(opts.conf), not bool(pro_setup['conf'])])
                    ]
                )
                if check_pro_cfg:
                    generator, gen_status = AVR8Setup(verbose=verbose), False
                    print(
                        "{0} {1} [{2}]".format(
                            "[{0}]".format(self.name),
                            'Generating AVR8 project skeleton', opts.pro
                        )
                    )
                    gen_status = generator.gen_pro_setup(
                        pro_setup, verbose=verbose
                    )
                    if gen_status:
                        success_message(self.name, 'Done\n')
                        status = True
                    else:
                        error_message(self.name, 'Failed to generate project')
            else:
                error_message(self.name, 'project already exist !')
        else:
            error_message('gen_avr8', 'Tool is not operational')
        return True if status else False
