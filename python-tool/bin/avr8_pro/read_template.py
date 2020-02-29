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

    from ats_utilities.config.yaml.yaml2object import Yaml2Object
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
                __PROJECT - template/project structure
                __FORMAT - File format for template
                __template_dir - Absolute file path of template dir
                __pro_cfg - Yaml object for template/project description
            method:
                __init__ - Initial constructor
                read - Read a template and return a string representation
    """

    __slots__ = (
        'VERBOSE',
        '__TEMPLATE_DIR',
        '__PROJECT',
        '__FORMAT',
        '__template_dir',
        '__pro_cfg'
    )
    VERBOSE = 'GEN_AVR8::AVR8_PRO::READ_TEMPLATE'
    __TEMPLATE_DIR = '/../../conf/template/'
    __PROJECT = 'project.yaml'
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
            pro = "{0}/../../conf/{1}".format(
                current_dir, ReadTemplate.__PROJECT
            )
            self.__pro_cfg = Yaml2Object(pro)
        else:
            self.__template_dir = None
            self.__pro_cfg = None

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
        check_cfg = all([bool(self.__template_dir), bool(self.__pro_cfg)])
        if check_cfg:
            pro_cfg = self.__pro_cfg.read_configuration(verbose=verbose)
            for pro_sec in pro_cfg:
                pro_cfg[pro_sec] = pro_cfg[pro_sec].split(' ')
            zip_tmp_pro = zip(pro_cfg['templates'], pro_cfg['modules'])
            for tmp_item, pro_item in zip_tmp_pro:
                iteam_list = []
                template_file = "{0}{1}".format(self.__template_dir, tmp_item)
                template_file_exists = self.check_file(
                    file_path=template_file, verbose=verbose
                )
                if template_file_exists:
                    with open(template_file, 'r') as tmpl:
                        iteam_list.append(pro_item)
                        iteam_list.append(tmpl.read())
                        setup_content[template_file] = iteam_list
        return setup_content

