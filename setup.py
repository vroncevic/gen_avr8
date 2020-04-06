#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
 Module
     setup.py
 Copyright
     Copyright (C) 2019 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Define setup for gen_avr8 package.
"""

from setuptools import setup

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2019, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'

setup(
    name='gen_avr8',
    version='1.1.0',
    description='Python package for generation of AVR8 project',
    author='Vladimir Roncevic',
    author_email='elektron.ronca@gmail.com',
    url='https://vroncevic.github.io/gen_avr8/',
    license='GPL 2019 Free software to use and distributed it.',
    long_description='Package gen_avr8 for python App/Tool/Script.',
    keywords='AVR, AVR8, Atmel, Microchip',
    platforms='POSIX',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'License :: OSI Approved :: GPL',
        'Operating System :: OS Independent',
    ],
    packages=[
        'gen_avr8',
        'gen_avr8.avr8_pro',
    ], requires=['colorama', 'bs4', 'yaml', 'configparser', 'pathlib'],
    package_data={
        'gen_avr8.conf': ['*'],
        'gen_avr8.log': ['*.']
    }
)
