# Create avr8 project skeleton

<img align="right" src="https://raw.githubusercontent.com/vroncevic/gen_avr8/dev/docs/gen_avr8_logo.png" width="25%">

**gen_avr8** is tool for creating avr8 project skeleton.

Developed in **[python](https://www.python.org/)** code.

The README is used to introduce the tool and provide instructions on
how to install the tool, any machine dependencies it may have and any
other information that should be provided before the tool is installed.

[![gen_avr8 python checker](https://github.com/vroncevic/gen_avr8/actions/workflows/gen_avr8_python_checker.yml/badge.svg)](https://github.com/vroncevic/gen_avr8/actions/workflows/gen_avr8_python_checker.yml) [![gen_avr8 package checker](https://github.com/vroncevic/gen_avr8/actions/workflows/gen_avr8_package_checker.yml/badge.svg)](https://github.com/vroncevic/gen_avr8/actions/workflows/gen_avr8_package.yml) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/gen_avr8.svg)](https://github.com/vroncevic/gen_avr8/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/gen_avr8.svg)](https://github.com/vroncevic/gen_avr8/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [🚀 Installation](#-installation)
    - [Install using pip](#install-using-pip)
    - [Install using build](#install-using-build)
    - [Install using py setup](#install-using-py-setup)
    - [Install using docker](#install-using-docker)
- [📦 Dependencies](#-dependencies)
- [📁 Tool structure](#-tool-structure)
  - [✨ Features](#-features)
- [📊 Code coverage](#-code-coverage)
- [🛠 Usage](#-usage)
- [📚 Docs](#-docs)
- [👥 Contributing](#-contributing)
- [📄 Copyright and licence](#-copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### 🚀 Installation

Used next development environment

![debian linux os](https://raw.githubusercontent.com/vroncevic/gen_avr8/dev/docs/debtux.png)

[![gen_avr8 python3 build](https://github.com/vroncevic/gen_avr8/actions/workflows/gen_avr8_python3_build.yml/badge.svg)](https://github.com/vroncevic/gen_avr8/actions/workflows/gen_avr8_python3_build.yml)

Currently there are four ways to install package
* Install process based on using pip mechanism
* Install process based on build mechanism
* Install process based on setup.py mechanism
* Install process based on docker mechanism

##### Install using pip

**gen_avr8** is located at **[pypi.org](https://pypi.org/project/gen_avr8/)**.

You can install by using pip

```bash
# python3
pip3 install gen_avr8
```

##### Install using build

Navigate to release **[page](https://github.com/vroncevic/gen_avr8/releases/)** download and extract release archive.

To install **gen_avr8** type the following

```bash
tar xvzf gen_avr8-x.y.z.tar.gz
cd gen_avr8-x.y.z/
# python3
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py 
# python3
python3 get-pip.py
python3 -m pip install --upgrade setuptools
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
pip3 install -r requirements.txt
python3 -m build --no-isolation --wheel
pip3 install ./dist/gen_avr8-*-py3-none-any.whl
rm -f get-pip.py
```

##### Install using py setup

Navigate to **[release page](https://github.com/vroncevic/gen_avr8/releases)** download and extract release archive.

To install **gen_avr8** locate and run setup.py with arguments

```bash
tar xvzf gen_avr8-x.y.z.tar.gz
cd gen_avr8-x.y.z
# python3
pip3 install -r requirements.txt
python3 setup.py install_lib
python3 setup.py install_egg_info
```

##### Install using docker

You can use Dockerfile to create image/container.

### 📦 Dependencies

**gen_avr8** requires next modules and libraries

* [ats-utilities - Python App/Tool/Script Utilities](https://pypi.org/project/ats-utilities/)

### 📁 Tool structure

**gen_avr8** is based on OOP.

Tool structure

<details>
<summary><b>Click to expand framework structure</b></summary>

```bash
    gen_avr8/
         ├── core/
         │   ├── __init__.py
         │   ├── model/
         │   │   ├── __init__.py
         │   │   └── project_setup.py
         │   └── service/
         │       ├── engine.py
         │       ├── __init__.py
         │       ├── iservice.py
         │       └── isubprocessor.py
         ├── engine.py
         ├── infrastructure/
         │   ├── cli/
         │   │   ├── engine.py
         │   │   ├── icli.py
         │   │   ├── __init__.py
         │   │   └── setup/
         │   │       ├── bundle.py
         │   │       ├── dep_validator.py
         │   │       ├── dependencies.py
         │   │       ├── factory.py
         │   │       ├── __init__.py
         │   │       ├── keys.py
         │   │       ├── opt_validator.py
         │   │       ├── options.py
         │   │       ├── registry.py
         │   │       └── validator.py
         │   ├── command/
         │   │   ├── command.py
         │   │   ├── gen_avr8_command_definition.py
         │   │   ├── gen_avr8_command_executor.py
         │   │   ├── icommand_definition.py
         │   │   ├── icommand_executor.py
         │   │   └── __init__.py
         │   ├── config/
         │   │   ├── gen_avr8.cfg
         │   │   ├── gen_avr8.logo
         │   │   ├── scheme.json
         │   │   └── templates.tgz
         │   ├── __init__.py
         │   └── subprocessor.py
         ├── __init__.py
         ├── py.typed
         └── setup/
             ├── bundle.py
             ├── dep_validator.py
             ├── dependencies.py
             ├── factory.py
             ├── __init__.py
             ├── keys.py
             ├── opt_validator.py
             ├── options.py
             ├── registry.py
             └── validator.py

      10 directories, 45 files
```
</details>

#### ✨ Features

* Automatically scaffolds ARM 32-bit assembly projects with build/make files.
* Provides a modular and extensible architecture based on OOP and SOLID principles.
* Includes command line interface (CLI) support via a command/executor structure.
* Robust validation of project bundles, dependencies, and options.
* Comes with configurable templates and JSON schema definitions.
* High code quality with full type checking and 100% unit test coverage.

### 📊 Code coverage

<details>
<summary><b>Click to expand code coverage</b></summary>

| Name | Stmts | Miss | Cover |
|------|-------|------|-------|
| `gen_avr8/__init__.py` | 8 | 0 | 100%|
| `gen_avr8/core/__init__.py` | 9 | 0 | 100%|
| `gen_avr8/core/model/__init__.py` | 9 | 0 | 100%|
| `gen_avr8/core/model/project_setup.py` | 14 | 0 | 100%|
| `gen_avr8/core/service/__init__.py` | 9 | 0 | 100%|
| `gen_avr8/core/service/engine.py` | 27 | 3 | 89%|
| `gen_avr8/core/service/iservice.py` | 14 | 0 | 100%|
| `gen_avr8/core/service/isubprocessor.py` | 14 | 0 | 100%|
| `gen_avr8/engine.py` | 57 | 0 | 100%|
| `gen_avr8/infrastructure/__init__.py` | 8 | 0 | 100%|
| `gen_avr8/infrastructure/cli/__init__.py` | 9 | 0 | 100%|
| `gen_avr8/infrastructure/cli/engine.py` | 39 | 7 | 82%|
| `gen_avr8/infrastructure/cli/icli.py` | 16 | 2 | 88%|
| `gen_avr8/infrastructure/cli/setup/__init__.py` | 9 | 0 | 100%|
| `gen_avr8/infrastructure/cli/setup/bundle.py` | 22 | 1 | 95%|
| `gen_avr8/infrastructure/cli/setup/dep_validator.py` | 28 | 0 | 100%|
| `gen_avr8/infrastructure/cli/setup/dependencies.py` | 18 | 0 | 100%|
| `gen_avr8/infrastructure/cli/setup/factory.py` | 32 | 32 | 0%|
| `gen_avr8/infrastructure/cli/setup/keys.py` | 26 | 1 | 96%|
| `gen_avr8/infrastructure/cli/setup/opt_validator.py` | 28 | 28 | 0%|
| `gen_avr8/infrastructure/cli/setup/options.py` | 15 | 15 | 0%|
| `gen_avr8/infrastructure/cli/setup/registry.py` | 21 | 0 | 100%|
| `gen_avr8/infrastructure/cli/setup/validator.py` | 35 | 0 | 100%|
| `gen_avr8/infrastructure/command/__init__.py` | 9 | 0 | 100%|
| `gen_avr8/infrastructure/command/command.py` | 16 | 0 | 100%|
| `gen_avr8/infrastructure/command/gen_avr8_command_definition.py` | 24 | 1 | 96%|
| `gen_avr8/infrastructure/command/gen_avr8_command_executor.py` | 21 | 2 | 90%|
| `gen_avr8/infrastructure/command/icommand_definition.py` | 15 | 0 | 100%|
| `gen_avr8/infrastructure/command/icommand_executor.py` | 14 | 1 | 93%|
| `gen_avr8/infrastructure/subprocessor.py` | 55 | 19 | 65%|
| `gen_avr8/setup/__init__.py` | 9 | 0 | 100%|
| `gen_avr8/setup/bundle.py` | 23 | 1 | 96%|
| `gen_avr8/setup/dep_validator.py` | 28 | 0 | 100%|
| `gen_avr8/setup/dependencies.py` | 19 | 0 | 100%|
| `gen_avr8/setup/factory.py` | 45 | 1 | 98%|
| `gen_avr8/setup/keys.py` | 27 | 1 | 96%|
| `gen_avr8/setup/opt_validator.py` | 26 | 9 | 65%|
| `gen_avr8/setup/options.py` | 12 | 0 | 100%|
| `gen_avr8/setup/registry.py` | 29 | 0 | 100%|
| `gen_avr8/setup/validator.py` | 40 | 0 | 100%|
| **Total** | 879 | 124 | 86% |

</details>

### 🛠 Usage

Install package

```bash
pip3 install gen_avr8
```

Prepare main entry point by downloading [main.py](https://raw.githubusercontent.com/vroncevic/gen_avr8/main/main.py) or create your own.


```bash
wget -O main.py https://raw.githubusercontent.com/vroncevic/gen_avr8/main/main.py
```

Running tool for creating new ARM Pico M project

```bash
python3 main.py create --name mytool --output ./demo/
```

### 📚 Docs

[![Documentation Status](https://readthedocs.org/projects/gen-avr8/badge/?version=latest)](https://gen-avr8.readthedocs.io/en/latest/?badge=latest)

More documentation and info at

* [gen_avr8.readthedocs.io](https://gen-avr8.readthedocs.io)
* [www.python.org](https://www.python.org/)

### 👥 Contributing

[Contributing to gen_avr8](CONTRIBUTING.md)

### 📄 Copyright and licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2025 - 2026 by [vroncevic.github.io/gen_avr8](https://vroncevic.github.io/gen_avr8/)

**gen_avr8** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/gen_avr8/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.python.org/psf/donations/)
