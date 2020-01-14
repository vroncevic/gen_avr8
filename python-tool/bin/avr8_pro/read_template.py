# -*- coding: UTF-8 -*-
# read_template.py
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
from os.path import isdir

try:
    from pathlib import Path

    from ats_utilities.config.file_checking import FileChecking
    from ats_utilities.console_io.verbose import verbose_message
except ImportError as e:
    msg = "\n{0}\n{1}\n".format(__file__, e)
    sys.exit(msg)  # Force close python ATS ##################################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2020, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ReadTemplate(FileChecking):
    """
        Define class ReadTemplate with attribute(s) and method(s).
        Read a template files and return a content.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                __TEMPLATE_DIR - Template dir path
                __TEMPLATES - Types of templates
                __FORMAT - File format for template
                __template_dir - Absolute file path of template dir
            method:
                __init__ - Initial constructor
                read - Read a template and return a string representation
    """

    __slots__ = (
        'VERBOSE',
        '__TEMPLATE_DIR',
        '__TEMPLATES',
        '__FORMAT',
        '__template_dir'
    )
    VERBOSE = 'GEN_AVR8::AVR8_PRO::READ_TEMPLATE'
    __TEMPLATE_DIR = '/../../conf/template/'
    __TEMPLATES = {
        1: 'module.template',
        2: 'sources.template',
        3: 'objects.template',
        4: 'subdir.template',
        5: 'Makefile.template'
    }
    __FORMAT = 'template'

    def __init__(self, verbose=False):
        """
            Setting template dir from configuration directory.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(
            ReadTemplate.VERBOSE, verbose, 'Initial reader'
        )
        FileChecking.__init__(self, verbose=verbose)
        current_dir = Path(__file__).parent
        template_dir = "{0}{1}".format(
            current_dir, ReadTemplate.__TEMPLATE_DIR
        )
        check_template_dir = isdir(template_dir)
        if check_template_dir:
            self.__template_dir = template_dir
        else:
            self.__template_dir = None

    def read(self, verbose=False):
        """
            Read template structure.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: Template content for setup module | None
            :rtype: <dict> | <NoneType>
            :exceptions: None
        """
        template_file_exists, setup_content, template_file = False, {}, None
        verbose_message(ReadTemplate.VERBOSE, verbose, 'Loading template')
        for tmp_index in ReadTemplate.__TEMPLATES.keys():
            template_file = "{0}{1}".format(
                self.__template_dir, ReadTemplate.__TEMPLATES[tmp_index]
            )
            template_file_exists = self.check_file(
                file_path=template_file, verbose=verbose
            )
            if template_file_exists:
                with open(template_file, 'r') as tmpl:
                    setup_content[tmp_index] = tmpl.read()
        return setup_content

