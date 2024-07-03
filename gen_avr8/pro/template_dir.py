# -*- coding: UTF-8 -*-

'''
Module
    template_dir.py
Copyright
    Copyright (C) 2018 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines class TemplateDir with attribute(s) and method(s).
    Creates an API for checking project template directory.
'''

import sys
from typing import List, Optional
from os.path import isdir, dirname, realpath

try:
    from ats_utilities.console_io.verbose import verbose_message
except ImportError as ats_error_message:
    # Force close python ATS ##################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/gen_avr8'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_avr8/blob/dev/LICENSE'
__version__ = '2.6.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TemplateDir:
    '''
        Defines class TemplateDir with attribute(s) and method(s).
        Creates an API for checking project template directory.

        It defines:

            :attributes:
                | _GEN_VERBOSE - Console text indicator for process-phase.
                | _CONF_DIR - Configuration directory path.
                | _TEMPLATE_DIR - Template directory path.
            :methods:
                | check_dir - Checks project directory.
                | setup_conf_dir - Sets configuration directory.
                | setup_template_dir - Sets template directory.
    '''

    _GEN_VERBOSE: str = 'GEN_AVR8::PRO::_TEMPLATE_DIR'
    _CONF_DIR: str = '/../conf/'
    _TEMPLATE_DIR: str = '/../conf/template/'

    @classmethod
    def check_dir(
        cls, target_dir: Optional[str], verbose: bool = False
    ) -> bool:
        '''
            Checks project directory.

            :param target_dir: Target directory to be checked | None
            :type target_dir: <Optional[str]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: True (directory ok) | False
            :rtype: <bool>
            :exceptions: None
        '''
        verbose_message(
            verbose, [f'{cls._GEN_VERBOSE.lower()} check project directory']
        )
        return isdir(f'{dirname(realpath(__file__))}{target_dir}')

    @classmethod
    def setup_conf_dir(cls, verbose: bool = False) -> Optional[str]:
        '''
            Sets configuration directory.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: Template directory | None
            :rtype: <Optional[str]>
            :exceptions: None
        '''
        conf_dir: Optional[str] = None
        if cls.check_dir(cls._CONF_DIR, verbose):
            conf_dir = f'{dirname(realpath(__file__))}{cls._CONF_DIR}'
            verbose_message(
                verbose, [f'{cls._GEN_VERBOSE.lower()} conf dir ', conf_dir]
            )
        return conf_dir

    @classmethod
    def setup_template_dir(cls, verbose: bool = False) -> Optional[str]:
        '''
            Sets template directory.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: Setup template directory | None
            :rtype: <Optional[str]>
            :exceptions: None
        '''
        template_dir: Optional[str] = None
        if cls.check_dir(cls._TEMPLATE_DIR, verbose):
            template_dir = f'{dirname(realpath(__file__))}{cls._TEMPLATE_DIR}'
            verbose_message(
                verbose, [
                    f'{cls._GEN_VERBOSE.lower()} template dir ', template_dir
                ]
            )
        return template_dir
