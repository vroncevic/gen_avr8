# -*- coding: UTF-8 -*-

'''
Module
    factory.py
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
    Factory for creating the gen_avr8 bundle.
'''

from __future__ import annotations

from ats_utilities.base.setup.factory import BaseBundleFactory
from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.base.setup.options import BaseBundleOptions
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.factory import ContextBundleFactory

from gen_avr8.setup.bundle import GenAVR8Bundle
from gen_avr8.setup.options import GenAVR8BundleOptions
from gen_avr8.setup.registry import GenAVR8BundleRegistry
from gen_avr8.setup.dependencies import GenAVR8BundleDependencies
from gen_avr8.setup.opt_validator import GenAVR8BundleOptionsValidator
from gen_avr8.setup.keys import GenAVR8BundleKeys
from gen_avr8.core.service.engine import Service
from gen_avr8.infrastructure.subprocessor import SubProcessor
from gen_avr8.infrastructure.cli.engine import CLI
from gen_avr8.infrastructure.cli.setup.bundle import CLIBundle
from gen_avr8.infrastructure.cli.setup.dependencies import CLIBundleDependencies
from gen_avr8.infrastructure.cli.setup.registry import CLIBundleRegistry
from gen_avr8.infrastructure.command.command import CommandBundle
from gen_avr8.infrastructure.command.gen_avr8_command_definition import GenAVR8CommandDefinition
from gen_avr8.infrastructure.command.gen_avr8_command_executor import GenAVR8CommandExecutor

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_avr8'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_avr8/blob/dev/LICENSE'
__version__ = '2.6.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenAVR8BundleFactory:
    '''
        Factory for creating the gen_avr8 bundle.

        It defines:

            :attributes:
                | _info_file - Path to the gen_avr8 info file.
            :methods:
                | create_bundle - Creates the gen_avr8 bundle with optional pre-configured options.
    '''

    _info_file: str = 'gen_avr8/infrastructure/config/gen_avr8.cfg'

    @classmethod
    def create_bundle(cls, options: GenAVR8BundleOptions | None = None) -> GenAVR8Bundle:
        '''
            Creates the gen_avr8 bundle with optional pre-configured options.

            :param options: The pre-configured options for the gen_avr8 bundle.
            :return: The gen_avr8 bundle.
            :exceptions:
                | ATSValueError: The gen_avr8 bundle options must be provided and have proper values.
                | ATSTypeError:  The gen_avr8 bundle options must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_avr8 bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The gen_avr8 bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_avr8 bundle must be provided and have proper values.
                | ATSTypeError:  The gen_avr8 bundle must be an instance of GenAVR8Bundle and
                |                its attributes must be instances of their respective types.
        '''
        if options is not None:
            GenAVR8BundleOptionsValidator.validate(options)

        info_file = options.get(GenAVR8BundleKeys.OPTION_INFO_FILE) if options else cls._info_file

        context_bundle: ContextBundle = ContextBundleFactory.create_bundle()

        base_bundle: BaseBundle = BaseBundleFactory.create_bundle(
            options=BaseBundleOptions(
                info_file=info_file,
                use_generator=True,
                context_bundle=context_bundle
            )
        )

        subprocessor: SubProcessor = SubProcessor(generator=base_bundle.generation_manager)

        service: Service = Service(subprocessor=subprocessor)

        gen_avr8_definition: GenAVR8CommandDefinition = GenAVR8CommandDefinition()

        gen_avr8_bundle: CommandBundle = CommandBundle(
            definition=gen_avr8_definition,
            executor=GenAVR8CommandExecutor(gen_avr8_definition)
        )

        cli_bundle: CLIBundle = CLIBundleRegistry.create_bundle(
            dependencies=CLIBundleDependencies(
                service=service,
                parser=base_bundle.option_manager,
                commands=[gen_avr8_bundle]
            )
        )

        cli: CLI = CLI(cli_bundle)

        return GenAVR8BundleRegistry.create_bundle(
            dependencies=GenAVR8BundleDependencies(
                base=base_bundle,
                service=service,
                subprocessor=subprocessor,
                cli=cli
            )
        )
