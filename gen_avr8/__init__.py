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
    Defines class GenAVR8 with attribute(s) and method(s).
    Loads base information, creates a CLI interface, and runs operations.
'''

import sys
from typing import Any, Dict, List
from os import getcwd
from os.path import exists, dirname, realpath
from argparse import Namespace

try:
    from ats_utilities.splash import Splash
    from ats_utilities.logging import ATSLogger
    from ats_utilities.cli.cfg_cli import CfgCLI
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.console_io.success import success_message
    from gen_avr8.pro import AVR8Setup
except ImportError as ats_error_message:
    # Force close python ATS ##################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, https://vroncevic.github.io/gen_avr8'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_avr8/blob/dev/LICENSE'
__version__ = '2.4.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenAVR8(CfgCLI):
    '''
        Defines class GenAVR8 with attribute(s) and method(s).
        Loads base information, creates a CLI interface, and runs operations.

        It defines:

            :attributes:
                | _GEN_VERBOSE - Console text indicator for process-phase.
                | _CONFIG - Tool info file path.
                | _LOG - Tool log file path.
                | _LOGO - Logo for splash screen.
                | _OPS - List of tool options.
                | _logger - Logger object API.
            :methods:
                | __init__ - Initial GenAVR8 constructor.
                | process - process and run tool option.
    '''

    _GEN_VERBOSE: str = 'GEN_AVR8'
    _CONFIG: str = '/conf/gen_avr8.cfg'
    _LOG: str = '/log/gen_avr8.log'
    _LOGO: str = '/conf/gen_avr8.logo'
    _OPS: List[str] = [
        '-g', '--gen', '-t', '--type', '-v', '--verbose', '--version'
    ]

    def __init__(self, verbose: bool = False) -> None:
        '''
            Initial GenAVR8 constructor.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        current_dir: str = dirname(realpath(__file__))
        gen_avr8_property: Dict[Any, Any] = {
            'ats_organization': 'vroncevic',
            'ats_repository': 'gen_avr8',
            'ats_name': 'gen_avr8',
            'ats_logo_path': f'{current_dir}{self._LOGO}',
            'ats_use_github_infrastructure': True
        }
        Splash(gen_avr8_property, verbose)
        base_info: str = f'{current_dir}{self._CONFIG}'
        super().__init__(base_info, verbose)
        verbose_message(verbose, [f'{self._GEN_VERBOSE} init tool info'])
        self._logger: ATSLogger = ATSLogger(
            self._GEN_VERBOSE.lower(), f'{current_dir}{self._LOG}', verbose
        )
        if self.tool_operational:
            self.add_new_option(
                self._OPS[0], self._OPS[1], dest='gen',
                help='generate AVR8 project skeleton'
            )
            self.add_new_option(
                self._OPS[2], self._OPS[3], dest='type',
                help='set app/lib type of project'
            )
            self.add_new_option(
                self._OPS[4], self._OPS[5], action='store_true',
                default=False, help='activate verbose mode for generation'
            )
            self.add_new_option(
                self._OPS[6], action='version', version=__version__
            )

    def process(self, verbose: bool = False) -> bool:
        '''
            Process and run operation.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: True (success operation) | False
            :rtype: <bool>
            :exceptions: None
        '''
        status: bool = False
        if self.tool_operational:
            if len(sys.argv) >= 4:
                options: List[str] = [
                    arg for i, arg in enumerate(sys.argv) if i % 2 == 0
                ]
                if any(arg not in self._OPS for arg in options[1:]):
                    error_message(
                        [f'{self._GEN_VERBOSE} provide project name and type']
                    )
                    self._logger.write_log(
                        'provide project name and type', self._logger.ATS_ERROR
                    )
                    return status
            else:
                error_message(
                    [f'{self._GEN_VERBOSE} provide project name and type']
                )
                self._logger.write_log(
                    'provide project name and type', self._logger.ATS_ERROR
                )
                return status
            args: Any | Namespace = self.parse_args(sys.argv[2:])
            project_exists: bool = exists(
                f'{getcwd()}/{str(getattr(args, "gen"))}'
            )
            if not project_exists:
                if bool(getattr(args, 'gen')) and bool(getattr(args, 'type')):
                    generator: AVR8Setup = AVR8Setup(
                        verbose=getattr(args, 'verbose') or verbose
                    )
                    generator.project_setup(
                        str(getattr(args, 'gen')), str(getattr(args, 'type'))
                    )
                    print(
                        " ".join([
                            f'[{self._GEN_VERBOSE.lower()}]',
                            'gen AVR8 project skeleton',
                            str(getattr(args, 'type')),
                            str(getattr(args, 'gen'))
                        ])
                    )
                    status: bool = generator.gen_pro_setup(
                        verbose=getattr(args, 'verbose') or verbose
                    )
                    if status:
                        success_message([f'{self._GEN_VERBOSE} done\n'])
                        self._logger.write_log(
                            f'gen project {getattr(args, "gen")} done',
                            self._logger.ATS_INFO
                        )
                    else:
                        error_message(
                            [f'{self._GEN_VERBOSE} failed to generate project']
                        )
                        self._logger.write_log(
                            'generation failed', self._logger.ATS_ERROR
                        )
            else:
                error_message(
                    [f'{self._GEN_VERBOSE} project dir already exist']
                )
                self._logger.write_log(
                    'project dir already exist', self._logger.ATS_ERROR
                )
        else:
            error_message([f'{self._GEN_VERBOSE} tool is not operational'])
            self._logger.write_log(
                'tool is not operational', self._logger.ATS_ERROR
            )
        return status
