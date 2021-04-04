<img align="right" src="https://raw.githubusercontent.com/vroncevic/gen_avr8/dev/docs/gen_avr8_logo.png" width="25%">

# AVR project skeleton generator

**gen_avr8** is tool for generation of AVR8 project skeleton for development
of embedded applications.

Developed in **[python](https://www.python.org/)** code: **100%**.

The README is used to introduce the tool modules and provide instructions on
how to install the tool modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

![Python package](https://github.com/vroncevic/gen_avr8/workflows/Python%20package%20gen_avr8/badge.svg?branch=master) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/gen_avr8.svg)](https://github.com/vroncevic/gen_avr8/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/gen_avr8.svg)](https://github.com/vroncevic/gen_avr8/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
    - [Install using pip](#install-using-pip)
    - [Install using setuptools](#install-using-setuptools)
    - [Install using docker](#install-using-docker)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Supported MCUS](#supported-mcus)
- [Generation flow of project setup](#generation-flow-of-project-setup)
- [Tool structure](#tool-structure)
- [Docs](#docs)
- [Copyright and Licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

![Install Python2 Package gen_avr8](https://github.com/vroncevic/gen_avr8/workflows/Install%20Python2%20Package%20gen_avr8/badge.svg?branch=master) ![Install Python3 Package gen_avr8](https://github.com/vroncevic/gen_avr8/workflows/Install%20Python3%20Package%20gen_avr8/badge.svg?branch=master)

Currently there are three ways to install tool:
* Install process based on pip
* Install process based on setup.py (setuptools)
* Install process based on docker mechanism

##### Install using pip

Python package is located at **[pypi.org](https://pypi.org/project/gen_avr8/)**.

You can install by using pip
```
#python2
pip install gen_avr8
#python3
pip3 install gen_avr8
```

##### Install using setuptools

Navigate to **[release page](https://github.com/vroncevic/gen_avr8/releases)**, download and extract release archive to local host.

To install modules, locate and run setup.py, type the following:
```
tar xvzf gen_avr8-x.y.z.tar.gz
cd gen_avr8-x.y.z/
#python2
python setup.py install_lib
python setup.py install_data
python setup.py install_egg_info
#python3
python3 setup.py install_lib
python3 setup.py install_data
python3 setup.py install_egg_info
```

##### Install using docker

You can use Dockerfile to create image/container.

[![gen_avr8 docker checker](https://github.com/vroncevic/gen_avr8/workflows/gen_avr8%20docker%20checker/badge.svg)](https://github.com/vroncevic/gen_avr8/actions?query=workflow%3A%22gen_avr8+docker+checker%22)

### Dependencies
**gen_avr8** tool requires other modules/libraries:

* [ats-utilities - Python App/Tool/Script Utilities](https://vroncevic.github.io/ats_utilities)

### Usage
Short example of usage **gen_avr8** tool

Create workspace directory Blink:
```
mkdir Blink
cd Blink/
```

Crete AVR8 project files, by using parameters:
```
python gen_avr8_run.py -g Blink -t app
```

Running build process:
```
cd build/
make all
```

In case for missing subtool from toolchain, please install the following packages
with your favorite package manager:
* gcc-avr
* binutils-avr
* gdb-avr
* avr-libc
* avrdude

Install directly from the shell as root user (**[debian](https://www.debian.org/)**):
```
apt-get install gcc-avr binutils-avr gdb-avr avr-libc avrdude
```

### Supported MCUS
Current list of supported microcontrollers:
```
attiny2313    atmega128      at90s2313
attiny24      atmega1280     at90s2333
attiny25      atmega1281     at90s4414
attiny26      atmega1284p    at90s4433
attiny261     atmega16       at90s4434
attiny44      atmega163      at90s8515
attiny45      atmega164p     at90s8535
attiny461     atmega165
attiny84      atmega165p
attiny85      atmega168
attiny861     atmega169
              atmega169p
              atmega2560
              atmega2561
              atmega32
              atmega324p
              atmega325
              atmega3250
              atmega329
              atmega3290
              atmega32u4
              atmega48
              atmega64
              atmega640
              atmega644
              atmega644p
              atmega645
              atmega6450
              atmega649
              atmega6490
              atmega8
              atmega8515
              atmega8535
              atmega88
```

### Generation flow of project setup
Base flow of generation process:

![alt tag](https://raw.githubusercontent.com/vroncevic/gen_avr8/dev/docs/gen_avr8_flow.png)

### Tool structure
**gen_avr8** is based on Template mechanism:

![alt tag](https://raw.githubusercontent.com/vroncevic/gen_avr8/dev/docs/gen_avr8.png)

Generator structure:
```
gen_avr8/
├── conf/
│   ├── fosc.yaml
│   ├── gen_avr8.cfg
│   ├── gen_avr8_util.cfg
│   ├── mcu.yaml
│   ├── project_app.yaml
│   ├── project_lib.yaml
│   └── template/
│       ├── app/
│       │   ├── cflags.template
│       │   ├── csflags.template
│       │   ├── Makefile.template
│       │   ├── module.template
│       │   ├── objects.template
│       │   ├── ocflags.template
│       │   ├── odflags.template
│       │   ├── sources.template
│       │   ├── subdir.template
│       │   └── tools.template
│       └── lib/
│           ├── aflags.template
│           ├── avr_lib_c.template
│           ├── avr_lib_h.template
│           ├── cflags.template
│           ├── csflags.template
│           ├── Makefile.template
│           ├── objects.template
│           ├── ocflags.template
│           ├── odflags.template
│           ├── sources.template
│           ├── subdir.template
│           └── tools.template
├── __init__.py
├── log/
│   └── gen_avr8.log
├── pro/
│   ├── __init__.py
│   ├── mcu_selector.py
│   ├── module_type.py
│   ├── osc_selector.py
│   ├── read_template.py
│   ├── template_dir.py
│   ├── template_type.py
│   └── write_template.py
└── run/
    └── gen_avr8_run.py
```

### Docs

[![Documentation Status](https://readthedocs.org/projects/gen-avr8/badge/?version=latest)](https://gen-avr8.readthedocs.io/en/latest/?badge=latest)

More documentation and info at:

* [gen-avr8.readthedocs.io](https://gen-avr8.readthedocs.io/en/latest/)
* [www.python.org](https://www.python.org/)

### Copyright and Licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2019 by [vroncevic.github.io/gen_avr8](https://vroncevic.github.io/gen_avr8/)

**gen_avr8** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/gen_avr8/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2)
