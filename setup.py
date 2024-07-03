#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Module
    setup.py
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
    Defines setup for tool gen_avr8.
'''

from __future__ import print_function
from typing import List, Optional
from os.path import abspath, dirname, join
from setuptools import setup

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/gen_avr8'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_avr8/blob/dev/LICENSE'
__version__ = '2.6.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'

TOOL_DIR: str = 'gen_avr8/'
CONF: str = 'conf'
TEMPLATE: str = 'conf/template'
LOG: str = 'log'
THIS_DIR: str = abspath(dirname(__file__))
long_description: Optional[str] = None
with open(join(THIS_DIR, 'README.md'), encoding='utf-8') as readme:
    long_description = readme.read()
PROGRAMMING_LANG: str = 'Programming Language :: Python ::'
VERSIONS: List[str] = ['3.10', '3.11']
SUPPORTED_PY_VERSIONS: List[str] = [
    f'{PROGRAMMING_LANG} {VERSION}' for VERSION in VERSIONS
]
LICENSE_PREFIX: str = 'License :: OSI Approved ::'
LICENSES: List[str] = [
    'GNU Lesser General Public License v2 (LGPLv2)',
    'GNU Lesser General Public License v2 or later (LGPLv2+)',
    'GNU Lesser General Public License v3 (LGPLv3)',
    'GNU Lesser General Public License v3 or later (LGPLv3+)',
    'GNU Library or Lesser General Public License (LGPL)'
]
APPROVED_LICENSES: List[str] = [
    f'{LICENSE_PREFIX} {LICENSE}' for LICENSE in LICENSES
]
PYP_CLASSIFIERS: List[str] = SUPPORTED_PY_VERSIONS + APPROVED_LICENSES
setup(
    name='gen_avr8',
    version='2.6.1',
    description='Python package for generation of AVR8 project',
    author='Vladimir Roncevic',
    author_email='elektron.ronca@gmail.com',
    url='https://vroncevic.github.io/gen_avr8',
    license='GPL 2018 - 2024 Free software to use and distributed it.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='AVR, AVR8, Atmel, Microchip, Microcontroller',
    platforms='POSIX',
    classifiers=PYP_CLASSIFIERS,
    packages=['gen_avr8', 'gen_avr8.pro'],
    install_requires=['ats-utilities'],
    package_data={
        'gen_avr8': [
            'py.typed',
            f'{CONF}/gen_avr8.logo',
            f'{CONF}/gen_avr8.cfg',
            f'{CONF}/gen_avr8_util.cfg',
            f'{CONF}/fosc.yaml',
            f'{CONF}/mcu.yaml',
            f'{CONF}/project_app.yaml',
            f'{CONF}/project_lib.yaml',
            f'{TEMPLATE}/app/cflags.template',
            f'{TEMPLATE}/app/csflags.template',
            f'{TEMPLATE}/app/Makefile.template',
            f'{TEMPLATE}/app/module.template',
            f'{TEMPLATE}/app/objects.template',
            f'{TEMPLATE}/app/ocflags.template',
            f'{TEMPLATE}/app/odflags.template',
            f'{TEMPLATE}/app/sources.template',
            f'{TEMPLATE}/app/subdir.template',
            f'{TEMPLATE}/app/tools.template',
            f'{TEMPLATE}/lib/aflags.template',
            f'{TEMPLATE}/lib/cflags.template',
            f'{TEMPLATE}/lib/csflags.template',
            f'{TEMPLATE}/lib/Makefile.template',
            f'{TEMPLATE}/lib/avr_lib_c.template',
            f'{TEMPLATE}/lib/avr_lib_h.template',
            f'{TEMPLATE}/lib/objects.template',
            f'{TEMPLATE}/lib/ocflags.template',
            f'{TEMPLATE}/lib/odflags.template',
            f'{TEMPLATE}/lib/sources.template',
            f'{TEMPLATE}/lib/subdir.template',
            f'{TEMPLATE}/lib/tools.template',
            f'{LOG}/log/gen_avr8.log'
        ]
    },
    data_files=[(
        '/usr/local/bin/', [
            f'{TOOL_DIR}run/gen_avr8_run.py'
        ]
    )]
)
