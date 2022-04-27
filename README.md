<img align="right" src="https://raw.githubusercontent.com/vroncevic/gen_avr8/dev/docs/gen_avr8_logo.png" width="25%">

# AVR project skeleton generator

☯️ **gen_avr8** is tool for generation of AVR8 project skeleton for development
of embedded applications.

Developed in 🐍 **[python](https://www.python.org/)** code.

[![codecov](https://codecov.io/gh/vroncevic/gen_avr8/branch/dev/graph/badge.svg?token=Y6VSNLJ45R)](https://codecov.io/gh/vroncevic/gen_avr8)
[![circleci](https://circleci.com/gh/vroncevic/gen_avr8/tree/master.svg?style=svg)](https://circleci.com/gh/vroncevic/gen_avr8/tree/master)

The README is used to introduce the tool modules and provide instructions on
how to install the tool modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

[![gen_avr8 python checker](https://img.shields.io/github/workflow/status/vroncevic/gen_avr8/gen_avr8_python_checker?style=flat&label=gen_avr8%20python%20checker)](https://github.com/vroncevic/gen_avr8/actions/workflows/gen_avr8_python_checker.yml) [![gen_avr8 package checker](https://img.shields.io/github/workflow/status/vroncevic/gen_avr8/gen_avr8_package_checker?style=flat&label=gen_avr8%20package%20checker)](https://github.com/vroncevic/gen_avr8/actions/workflows/gen_avr8_package_checker.yml) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/gen_avr8.svg)](https://github.com/vroncevic/gen_avr8/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/gen_avr8.svg)](https://github.com/vroncevic/gen_avr8/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
    - [Install using pip](#install-using-pip)
    - [Install using build](#install-using-build)
    - [Install using py setup](#install-using-py-setup)
    - [Install using docker](#install-using-docker)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Supported MCUS](#supported-mcus)
- [Generation flow of project setup](#generation-flow-of-project-setup)
- [Tool structure](#tool-structure)
- [Docs](#docs)
- [Contributing](#contributing)
- [Copyright and Licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

Used next development environment

![debian linux os](https://raw.githubusercontent.com/vroncevic/gen_avr8/dev/docs/debtux.png)

[![gen_avr8 python2 build](https://img.shields.io/github/workflow/status/vroncevic/gen_avr8/gen_avr8_python2_build?style=flat&label=gen_avr8%20python2%20build)](https://github.com/vroncevic/gen_avr8/actions/workflows/gen_avr8_python2_build.yml) [![gen_avr8 python3 build](https://img.shields.io/github/workflow/status/vroncevic/gen_avr8/gen_avr8_python3_build?style=flat&label=gen_avr8%20python3%20build)](https://github.com/vroncevic/gen_avr8/actions/workflows/gen_avr8_python3_build.yml)

Currently there are three ways to install package
* Install process based on using pip mechanism
* Install process based on build mechanism
* Install process based on setup.py mechanism
* Install process based on docker mechanism

##### Install using pip

Python 📦 is located at **[pypi.org](https://pypi.org/project/gen-avr8/)**.

You can install by using pip

```bash
#python2
pip install gen-avr8
#python3
pip3 install gen-avr8
```

##### Install using build

Navigate to release **[page](https://github.com/vroncevic/gen_avr8/releases/)** download and extract release archive 📦.

To install **gen_avr8** 📦 type the following

```bash
tar xvzf gen_avr8-x.y.z.tar.gz
cd gen_avr8-x.y.z/
# python2
wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
python2 get-pip.py 
python2 -m pip install --upgrade setuptools
python2 -m pip install --upgrade pip
python2 -m pip install --upgrade build
pip2 install -r requirements.txt
python2 -m build --no-isolation --wheel
pip2 install ./dist/gen_avr8-*-py2-none-any.whl
rm -f get-pip.py
chmod 755 /usr/local/lib/python2.7/dist-packages/usr/local/bin/gen_avr8_run.py
ln -s /usr/local/lib/python2.7/dist-packages/usr/local/bin/gen_avr8_run.py /usr/local/bin/gen_avr8_run.py
# python3
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py 
python3 -m pip install --upgrade setuptools
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
pip3 install -r requirements.txt
python3 -m build --no-isolation --wheel
pip3 install ./dist/gen_avr8-*-py3-none-any.whl
rm -f get-pip.py
chmod 755 /usr/local/lib/python3.9/dist-packages/usr/local/bin/gen_avr8_run.py
ln -s /usr/local/lib/python3.9/dist-packages/usr/local/bin/gen_avr8_run.py /usr/local/bin/gen_avr8_run.py
```

##### Install using py setup

Navigate to **[release page](https://github.com/vroncevic/gen_avr8/releases)** download and extract release archive 📦.

To install **gen_avr8** 📦 locate and run setup.py with arguments

```bash
tar xvzf gen_avr8-x.y.z.tar.gz
cd gen_avr8-x.y.z
# python2
pip2 install -r requirements.txt
python2 setup.py install_lib
python2 setup.py install_egg_info
# python3
pip3 install -r requirements.txt
python3 setup.py install_lib
python3 setup.py install_egg_info
```

##### Install using docker

You can use Dockerfile to create image/container 🚢.

[![gen_avr8 docker checker](https://img.shields.io/github/workflow/status/vroncevic/gen_avr8/gen_avr8_docker_checker?style=flat&label=gen_avr8%20docker%20checker)](https://github.com/vroncevic/gen_avr8/actions/workflows/gen_avr8_docker_checker.yml)

### Dependencies

**gen_avr8** tool requires other modules/libraries

- [ats-utilities - Python App/Tool/Script Utilities](https://vroncevic.github.io/gen_avr8)

### Usage

Short example of usage **gen_avr8** tool

Create workspace directory Blink

```bash
mkdir Blink
cd Blink/
```

Crete AVR8 project files, by using parameters

```bash
python gen_avr8_run.py -g Blink -t app
```

Running build process

```bash
cd build/
make all
```

In case for missing subtool from toolchain, please install the following packages with your favorite package manager

- gcc-avr
- binutils-avr
- gdb-avr
- avr-libc
- avrdude

Install directly from the shell as root user (**[debian](https://www.debian.org/)**)

```bash
apt-get install gcc-avr binutils-avr gdb-avr avr-libc avrdude
```

### Supported MCUS

Current list of supported microcontrollers

```bash
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

Base flow of generation process

![Generation flow](https://raw.githubusercontent.com/vroncevic/gen_avr8/dev/docs/gen_avr8_flow.png)

### Tool structure

**gen_avr8** is based on Template mechanism

![Project modules](https://raw.githubusercontent.com/vroncevic/gen_avr8/dev/docs/gen_avr8.png)

🧰 Generator structure

```bash
gen_avr8/
├── conf/
|   ├── gen_avr8.logo
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

[![Documentation Status](https://readthedocs.org/projects/gen_avr8/badge/?version=latest)](https://gen_avr8.readthedocs.io/en/latest/?badge=latest)

📗 More documentation and info at

* [gen_avr8.readthedocs.io](https://gen_avr8.readthedocs.io/en/latest/)
* [www.python.org](https://www.python.org/)

### Contributing

🌎 🌍 🌏 [Contributing to gen_avr8](CONTRIBUTING.md)

### Copyright and Licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2018 by [vroncevic.github.io/gen_avr8](https://vroncevic.github.io/gen_avr8/)

**gen_avr8** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/gen_avr8/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2)
