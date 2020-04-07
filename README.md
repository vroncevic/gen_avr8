# AVR project skeleton generator.
**gen_avr8** is tool for generation of AVR8 project skeleton for development
of embedded applications.

Developed in python code: **100%**.

The README is used to introduce the tool modules and provide instructions on
how to install the tool modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

![Python package](https://github.com/vroncevic/gen_avr8/workflows/Python%20package/badge.svg)
 [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/gen_avr8.svg)](https://github.com/vroncevic/gen_avr8/issues)
 [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/gen_avr8.svg)](https://github.com/vroncevic/gen_avr8/graphs/contributors)


### TABLE OF CONTENTS

- [INSTALLATION](https://github.com/vroncevic/gen_avr8#installation)
    * [INSTALL USING SETUPTOOLS](https://github.com/vroncevic/gen_avr8#install-using-setuptools)
    * [INSTALL USING DOCKER](https://github.com/vroncevic/gen_avr8#install-using-docker)
- [USAGE](https://github.com/vroncevic/gen_avr8#usage)
- [DEPENDENCIES](https://github.com/vroncevic/gen_avr8#dependencies)
- [SUPPORTED MCUS](https://github.com/vroncevic/gen_avr8#supported-mcus)
- [GENERATION FLOW OF PROJECT SETUP](https://github.com/vroncevic/gen_avr8#generation-flow-of-project-setup)
- [TOOL STRUCTURE](https://github.com/vroncevic/gen_avr8#tool-structure)
- [DOCS](https://github.com/vroncevic/gen_avr8#docs)
- [COPYRIGHT AND LICENCE](https://github.com/vroncevic/gen_avr8#copyright-and-licence)

:sparkles:

### INSTALLATION
Navigate to **[release page](https://github.com/vroncevic/gen_avr8/releases)**, download and extract release archive to local host.

Currently there are two ways to install tool:
* Install process based on setup.py (setuptools)
* Install process based on docker mechanism

##### INSTALL USING SETUPTOOLS
To install this set of modules type the following:
```
tar xvzf gen_avr8-x.y.z.tar.gz
cd gen_avr8-x.y.z/
python setup.py install
```

##### INSTALL USING DOCKER
You can use docker to load Dockerfile which contains all the commands
a user could call on the command line to assemble an image.

:sparkles:

### DEPENDENCIES
gen_avr8 tool requires other modules/libraries:

* **ats_utilities**, url: https://vroncevic.github.io/ats_utilities

:sparkles:

### USAGE
Short example of usage gen_avr8 tool

Create workspace directory Blink:
```
mkdir Blink
cd Blink/
```

Create configuration file **avr8.yaml**, with next content:
```
MCU:
    atmega8
OSC:
    16000000UL
```

Crete AVR8 project files, by using parameters from yaml file:
```
python gen_avr8_run.py -g Blink -c avr8.yaml
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

Install directly from the shell as root user (**debian**):
```
apt-get install gcc-avr binutils-avr gdb-avr avr-libc avrdude
```

:sparkles:

### SUPPORTED MCUS
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

:sparkles:

### GENERATION FLOW OF PROJECT SETUP
Base flow of generation process:

![alt tag](https://raw.githubusercontent.com/vroncevic/gen_avr8/dev/docs/gen_avr8_flow.png)

:sparkles:

### TOOL STRUCTURE
gen_avr8 is based on Template mechanism:

![alt tag](https://raw.githubusercontent.com/vroncevic/gen_avr8/dev/docs/gen_avr8.png)

Generator structure:
```
gen_avr8/
├── avr8_pro/
│   ├── avr8_setup.py
│   ├── __init__.py
│   ├── mcu_selector.py
│   ├── osc_selector.py
│   ├── read_template.py
│   └── write_template.py
├── conf/
│   ├── fosc.yaml
│   ├── gen_avr8.cfg
│   ├── gen_avr8_util.cfg
│   ├── mcu.yaml
│   ├── project.yaml
│   └── template/
│       ├── cflags.template
│       ├── csflags.template
│       ├── Makefile.template
│       ├── module.template
│       ├── objects.template
│       ├── ocflags.template
│       ├── odflags.template
│       ├── sources.template
│       └── subdir.template
├── __init__.py
├── log/
│   └── gen_avr8.log
└── run/
    └── gen_avr8_run.py
```

:sparkles:

### DOCS

[![Documentation Status](https://readthedocs.org/projects/gen-avr8/badge/?version=latest)](https://gen-avr8.readthedocs.io/en/latest/?badge=latest)

More documentation and info at:

* https://gen-avr8.readthedocs.io/en/latest/

:sparkles:

### COPYRIGHT AND LICENCE

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2019 by https://vroncevic.github.io/gen_avr8/

This tool is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

:sparkles:
