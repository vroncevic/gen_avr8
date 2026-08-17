# -*- coding: UTF-8 -*-

'''
Module
    gen_avr8_command_executor.py
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
    Defines GenAVR8CommandExecutor class.
'''

from __future__ import annotations

from collections.abc import Mapping

from ats_utilities.utils.reflection import to_str

from gen_avr8.infrastructure.command.icommand_definition import ICommandDefinition
from gen_avr8.core.service.iservice import IService

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_avr8'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_avr8/blob/dev/LICENSE'
__version__ = '2.6.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenAVR8CommandExecutor:
    '''
        Command executor strategy for generating avr8 project files.

        It defines:

            :attributes:
                | definition - The command CLI metadata definition.
            :methods:
                | execute - Executes the subcommand.
                | __str__ - Returns the GenAVR8CommandExecutor as string representation.
    '''

    definition: ICommandDefinition

    def __init__(self, definition: ICommandDefinition) -> None:
        '''
            Initializes the command executor.

            :param definition: The command definition metadata.
        '''
        self.definition = definition

    def execute(self, *, params: Mapping[str, object], service: IService) -> Mapping[str, object]:
        '''
            Executes the subcommand.

            :param params: Subcommand parameters from CLI parser.
            :param service: Command orchestrator service instance.
            :return: The result of the subcommand execution.
        '''
        return service.execute(params=params) if service.is_initialized() else {
            'returncode': 1, 'stdout': '', 'stderr': 'service not initialized'
        }

    def __str__(self) -> str:
        '''
            Returns the GenAVR8CommandExecutor as string representation.

            :return: The GenAVR8CommandExecutor as string representation.
        '''
        return to_str(self)
