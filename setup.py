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
     Defined setup for tool gen_avr8.
'''

from __future__ import print_function
import sys
from os.path import abspath, dirname, join, exists
from setuptools import setup

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, https://vroncevic.github.io/gen_avr8'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_avr8/blob/dev/LICENSE'
__version__ = '1.8.3'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'

def install_directory():
    '''
        Return the installation directory, or None.

        :return: path (success) | None.
        :rtype: <str> | <NoneType>
        :exceptions: None
    '''
    py_version = '{0}.{1}'.format(sys.version_info[0], sys.version_info[1])
    if '--github' in sys.argv:
        index = sys.argv.index('--github')
        sys.argv.pop(index)
        paths = (
            '{0}/lib/python{1}/dist-packages/'.format(sys.prefix, py_version),
            '{0}/lib/python{1}/site-packages/'.format(sys.prefix, py_version)
        )
    else:
        paths = (s for s in (
            '{0}/local/lib/python{1}/dist-packages/'.format(
                sys.prefix, py_version
            ),
            '{0}/local/lib/python{1}/site-packages/'.format(
                sys.prefix, py_version
            )
        ))
    message = None
    for path in paths:
        message = '[setup] check path {0}'.format(path)
        print(message)
        if exists(path):
            message = '[setup] use path {0}'.format(path)
            print(message)
            return path
    message = '[setup] no installation path found, check {0}\n'.format(
        sys.prefix
    )
    print(message)
    return None

INSTALL_DIR = install_directory()
TOOL_DIR = 'gen_avr8/'
if not bool(INSTALL_DIR):
    print('[setup] force exit from install process')
    sys.exit(127)
THIS_DIR, LONG_DESCRIPTION = abspath(dirname(__file__)), None
with open(join(THIS_DIR, 'README.md')) as readme:
    LONG_DESCRIPTION = readme.read()
PROGRAMMING_LANG = 'Programming Language :: Python ::'
VERSIONS = ['2.7', '3', '3.2', '3.3', '3.4']
SUPPORTED_PY_VERSIONS = [
    '{0} {1}'.format(PROGRAMMING_LANG, VERSION) for VERSION in VERSIONS
]
LICENSE_PREFIX = 'License :: OSI Approved ::'
LICENSES = [
    'GNU Lesser General Public License v2 (LGPLv2)',
    'GNU Lesser General Public License v2 or later (LGPLv2+)',
    'GNU Lesser General Public License v3 (LGPLv3)',
    'GNU Lesser General Public License v3 or later (LGPLv3+)',
    'GNU Library or Lesser General Public License (LGPL)'
]
APPROVED_LICENSES = [
    '{0} {1}'.format(LICENSE_PREFIX, LICENSE) for LICENSE in LICENSES
]
PYP_CLASSIFIERS = SUPPORTED_PY_VERSIONS + APPROVED_LICENSES
setup(
    name='gen_avr8',
    version='1.8.3',
    description='Python package for generation of AVR8 project',
    author='Vladimir Roncevic',
    author_email='elektron.ronca@gmail.com',
    url='https://vroncevic.github.io/gen_avr8',
    license='GPL 2018 Free software to use and distributed it.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    keywords='AVR, AVR8, Atmel, Microchip, Microcontroller',
    platforms='POSIX',
    classifiers=PYP_CLASSIFIERS,
    packages=['gen_avr8', 'gen_avr8.pro'],
    install_requires=['ats-utilities'],
    package_data = {
        'gen_avr8': [
            'conf/gen_avr8.cfg',
            'conf/gen_avr8_util.cfg',
            'conf/fosc.yaml',
            'conf/mcu.yaml',
            'conf/project_app.yaml',
            'conf/project_lib.yaml',
            'conf/template/app/cflags.template',
            'conf/template/app/csflags.template',
            'conf/template/app/Makefile.template',
            'conf/template/app/module.template',
            'conf/template/app/objects.template',
            'conf/template/app/ocflags.template',
            'conf/template/app/odflags.template',
            'conf/template/app/sources.template',
            'conf/template/app/subdir.template',
            'conf/template/app/tools.template',
            'conf/template/lib/aflags.template',
            'conf/template/lib/cflags.template',
            'conf/template/lib/csflags.template',
            'conf/template/lib/Makefile.template',
            'conf/template/lib/avr_lib_c.template',
            'conf/template/lib/avr_lib_h.template',
            'conf/template/lib/objects.template',
            'conf/template/lib/ocflags.template',
            'conf/template/lib/odflags.template',
            'conf/template/lib/sources.template',
            'conf/template/lib/subdir.template',
            'conf/template/lib/tools.template',
            'log/gen_avr8.log'
        ]
    },
    data_files=[
        (
            '/usr/local/bin/', [
                '{0}{1}'.format(TOOL_DIR, 'run/gen_avr8_run.py')
            ]
        )
    ]
)
