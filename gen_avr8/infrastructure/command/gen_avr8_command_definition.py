# -*- coding: UTF-8 -*-

'''
Module
    gen_avr8_command_definition.py
Copyright
    Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines GenAVR8CommandDefinition class.
'''

from __future__ import annotations

from collections.abc import Sequence

from ats_utilities.option.command.data import OptionData
from ats_utilities.utils.reflection import to_str

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_avr8'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_avr8/blob/dev/LICENSE'
__version__ = '2.6.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenAVR8CommandDefinition:
    '''
        CLI subcommand metadata definition for avr8 project generation.

        It defines:

            :methods:
                | name - Returns the command name.
                | help_text - Returns the command help text.
                | options - Returns the sequence of command options.
                | __str__ - Returns the command definition as string representation.
    '''

    @property
    def name(self) -> str:
        '''
            Returns the command name.

            :return: The command name.
        '''
        return 'create'

    @property
    def help_text(self) -> str:
        '''
            Returns the command help text.

            :return: The command help text.
        '''
        return 'Generate AVR8 project files'

    @property
    def options(self) -> Sequence[OptionData]:
        '''
            Returns the command options.

            :return: Sequence of command options.
        '''
        return [
            OptionData(
                name="--name",
                help_text="AVR8 project name",
                action=None,
                default="myapp",
                required=True,
                choices=None,
                nargs=None
            ),
            OptionData(
                name="--type",
                help_text="AVR8 project type (app/lib)",
                action=None,
                default="app",
                required=True,
                choices=None,
                nargs=None
            ),
            OptionData(
                name="--output",
                help_text="Path to the output directory",
                action=None,
                default="./",
                required=True,
                choices=None,
                nargs=None
            )
        ]

    def __str__(self) -> str:
        '''
            Returns the command definition as string representation.

            :return: The command definition as string representation.
        '''
        return to_str(self)
