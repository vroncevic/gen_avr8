# -*- coding: utf-8 -*-

'''
 Module
     __init__.py
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
     Defined class GenAVR8 with attribute(s) and method(s).
     Load a base info, create an CLI interface and run operation(s).
'''

import sys

try:
    from pathlib import Path
    from gen_avr8.pro import AVR8Setup
    from ats_utilities.cli.cfg_cli import CfgCLI
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.console_io.success import success_message
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


class GenAVR8(CfgCLI):
    '''
        Defined class GenAVR8 with attribute(s) and method(s).
        Load a base info, create an CLI interface and run operation(s).
        It defines:

            :attributes:
                | __slots__ - Setting class slots.
                | VERBOSE - Console text indicator for current process-phase.
                | __CONFIG - Tool info file path.
                | __OPS - Tool options (list).
            :methods:
                | __init__ - Initial constructor.
                | process - Process and run tool option.
                | __str__ - Dunder method for GenAVR8.
    '''

    __slots__ = ('VERBOSE', '__CONFIG', '__OPS')
    VERBOSE = 'GEN_AVR8'
    __CONFIG = '/conf/gen_avr8.cfg'
    __OPS = ['-g', '--gen', '-t', '--type', '-v']

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        verbose_message(GenAVR8.VERBOSE, verbose, 'init tool info')
        current_dir = Path(__file__).resolve().parent
        base_info = '{0}{1}'.format(current_dir, GenAVR8.__CONFIG)
        CfgCLI.__init__(self, base_info, verbose=verbose)
        if self.tool_operational:
            self.add_new_option(
                GenAVR8.__OPS[0], GenAVR8.__OPS[1], dest='pro',
                help='generate AVR8 project skeleton'
            )
            self.add_new_option(
                GenAVR8.__OPS[2], GenAVR8.__OPS[3], dest='type',
                help='set app/lib type of project'
            )
            self.add_new_option(
                GenAVR8.__OPS[4], action='store_true', default=False,
                help='activate verbose mode for generation'
            )

    def process(self, verbose=False):
        '''
            Process and run operation.

            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :return: True (success) | False.
            :rtype: <bool>
            :exceptions: None
        '''
        status = False
        if self.tool_operational:
            if len(sys.argv) >= 4:
                options = [arg for i, arg in enumerate(sys.argv) if i %2 != 0]
                if any([arg not in GenAVR8.__OPS for arg in options]):
                    sys.argv = []
                    sys.argv.append('-h')
            else:
                sys.argv.append('-h')
            opts, args = self.parse_args(sys.argv)
            if bool(opts.gen) and bool(opts.type):
                pro_setup = {}
                pro_setup['name'] = opts.pro
                pro_setup['type'] = opts.type
                if all([bool(pro_setup['name']), bool(pro_setup['type'])]):
                    generator = AVR8Setup(verbose=opts.v or verbose)
                    generator.project_setup = pro_setup
                    print(
                        '{0} {1} {2} [{3}]'.format(
                            '[{0}]'.format(GenAVR8.VERBOSE.lower()),
                            'generating AVR8 project skeleton',
                            opts.type, opts.pro
                        )
                    )
                    status = generator.gen_pro_setup(verbose=opts.v or verbose)
                    if status:
                        success_message(GenAVR8.VERBOSE, 'done\n')
                    else:
                        error_message(
                            GenAVR8.VERBOSE, 'failed to generate project'
                        )
            else:
                error_message(GenAVR8.VERBOSE, 'failed to generate project')
        else:
            error_message(GenAVR8.VERBOSE, 'tool is not operational')
        return True if status else False

    def __str__(self):
        '''
            Dunder method for GenAVR8.

            :return: Object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1})'.format(
            self.__class__.__name__, CfgCLI.__str__(self)
        )
