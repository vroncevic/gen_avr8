#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Module
    setup.py
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
    Defines setup for tool gen_avr8.
'''

from __future__ import print_function
import sys
from os.path import abspath, dirname, join, exists
from setuptools import setup

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, https://vroncevic.github.io/gen_avr8'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_avr8/blob/dev/LICENSE'
__version__ = '2.4.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


def install_directory() -> str | None:
    '''
        Return the installation directory, or None.

        :return: Path (success) | None
        :rtype: <str> | <NoneType>
        :exceptions: None
    '''
    py_version: str = f'{sys.version_info[0]}.{sys.version_info[1]}'
    if py_version:
        if '--github' in sys.argv:
            index: int = sys.argv.index('--github')
            sys.argv.pop(index)
            paths = (
                f'{sys.prefix}/lib/python{py_version}/dist-packages/',
                f'{sys.prefix}/lib/python{py_version}/site-packages/'
            )
        else:
            paths = (s for s in (
                f'{sys.prefix}/local/lib/python{py_version}/dist-packages/',
                f'{sys.prefix}/local/lib/python{py_version}/site-packages/'
            ))
        message: str | None = None
        for path in paths:
            message = f'[setup] check path {path}'
            print(message)
            if exists(path):
                message = f'[setup] use path {path}'
                print(message)
                return path
        message = f'[setup] no install path found, check {sys.prefix}\n'
        print(message)
    return None


INSTALL_DIR: str | None = install_directory()
TOOL_DIR: str = 'gen_avr8/'
CONF: str = 'conf'
TEMPLATE: str = 'conf/template'
LOG: str = 'log'
if not INSTALL_DIR:
    print('[setup] force exit from install process')
    sys.exit(127)
THIS_DIR: str = abspath(dirname(__file__))
long_description: str | None = None
with open(join(THIS_DIR, 'README.md'), encoding='utf-8') as readme:
    long_description = readme.read()
PROGRAMMING_LANG = 'Programming Language :: Python ::'
VERSIONS: list[str] = ['3.10', '3.11']
SUPPORTED_PY_VERSIONS: list[str] = [
    f'{PROGRAMMING_LANG} {VERSION}' for VERSION in VERSIONS
]
LICENSE_PREFIX = 'License :: OSI Approved ::'
LICENSES: list[str] = [
    'GNU Lesser General Public License v2 (LGPLv2)',
    'GNU Lesser General Public License v2 or later (LGPLv2+)',
    'GNU Lesser General Public License v3 (LGPLv3)',
    'GNU Lesser General Public License v3 or later (LGPLv3+)',
    'GNU Library or Lesser General Public License (LGPL)'
]
APPROVED_LICENSES: list[str] = [
    f'{LICENSE_PREFIX} {LICENSE}' for LICENSE in LICENSES
]
PYP_CLASSIFIERS: list[str] = SUPPORTED_PY_VERSIONS + APPROVED_LICENSES
setup(
    name='gen_avr8',
    version='2.4.5',
    description='Python package for generation of AVR8 project',
    author='Vladimir Roncevic',
    author_email='elektron.ronca@gmail.com',
    url='https://vroncevic.github.io/gen_avr8',
    license='GPL 2018 Free software to use and distributed it.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='AVR, AVR8, Atmel, Microchip, Microcontroller',
    platforms='POSIX',
    classifiers=PYP_CLASSIFIERS,
    packages=['gen_avr8', 'gen_avr8.pro'],
    install_requires=['ats-utilities'],
    package_data={
        'gen_avr8': [
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
