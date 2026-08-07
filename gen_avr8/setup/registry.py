# -*- coding: UTF-8 -*-

'''
Module
    registry.py
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
    Encapsulates core gen_avr8 components for simplification of gen_avr8 bundle.
'''

from __future__ import annotations

from ats_utilities.base.setup.bundle import BaseBundle

from gen_avr8.core.service.iservice import IService
from gen_avr8.core.service.isubprocessor import ISubProcessor
from gen_avr8.infrastructure.cli.icli import ICLI
from gen_avr8.setup.bundle import GenAVR8Bundle
from gen_avr8.setup.validator import GenAVR8BundleValidator
from gen_avr8.setup.keys import GenAVR8BundleKeys
from gen_avr8.setup.dependencies import GenAVR8BundleDependencies
from gen_avr8.setup.dep_validator import GenAVR8BundleDependenciesValidator

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_avr8'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_avr8/blob/dev/LICENSE'
__version__ = '2.6.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenAVR8BundleRegistry:
    '''
        Encapsulates core gen_avr8 components for simplification of gen_avr8 bundle.

        It defines:

            :methods:
                | create_bundle - Creates the gen_avr8 bundle.
    '''

    @classmethod
    def create_bundle(cls, dependencies: GenAVR8BundleDependencies) -> GenAVR8Bundle:
        '''
            Creates the gen_avr8 bundle.

            :param dependencies: The gen_avr8 bundle dependencies.
            :return: The gen_avr8 bundle.
            :exceptions:
                | ATSValueError: The gen_avr8 bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The gen_avr8 bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_avr8 bundle must be provided and have proper values.
                | ATSTypeError:  The gen_avr8 bundle must be an instance of GenAVR8Bundle and
                |                its attributes must be instances of their respective types.
        '''
        GenAVR8BundleDependenciesValidator.validate(dependencies)

        base: BaseBundle | None = dependencies.get(GenAVR8BundleKeys.DEPENDENCY_BASE) if dependencies else None
        service: IService | None = dependencies.get(GenAVR8BundleKeys.DEPENDENCY_SERVICE) if dependencies else None
        subprocessor: ISubProcessor | None = dependencies.get(GenAVR8BundleKeys.DEPENDENCY_SUBPROCESSOR) if dependencies else None
        cli: ICLI | None = dependencies.get(GenAVR8BundleKeys.DEPENDENCY_CLI) if dependencies else None

        bundle: GenAVR8Bundle = GenAVR8Bundle(base=base, service=service, subprocessor=subprocessor, cli=cli)

        GenAVR8BundleValidator.validate(bundle)

        return bundle
