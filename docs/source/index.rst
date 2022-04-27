AVR project skeleton generator
===============================

☯️ **gen_avr8** is toolset for generation of AVR8 project skeleton for
development embedded applications.

Developed in 🐍 `python <https://www.python.org/>`_ code.

The README is used to introduce the tool modules and provide instructions on
how to install the tool modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|python package| |github issues| |documentation status| |github contributors|

.. |python package| image:: https://img.shields.io/github/workflow/status/vroncevic/gen_avr8/gen_avr8_python_checker?style=flat&label=gen_avr8%20python%20checker
   :target: https://img.shields.io/github/workflow/status/vroncevic/gen_avr8/gen_avr8_python_checker

.. |github issues| image:: https://img.shields.io/github/workflow/status/vroncevic/gen_avr8/gen_avr8_package_checker?style=flat&label=gen_avr8%20package%20checker
   :target: https://img.shields.io/github/workflow/status/vroncevic/gen_avr8/gen_avr8_package_checker

.. |github contributors| image:: https://img.shields.io/github/contributors/vroncevic/gen_avr8.svg
   :target: https://github.com/vroncevic/gen_avr8/graphs/contributors

.. |documentation status| image:: https://readthedocs.org/projects/gen_avr8/badge/?version=latest
   :target: https://gen_avr8.readthedocs.io/projects/gen_avr8/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents

   modules
   self

Installation
-------------

|install python2 package| |install python3 package|

.. |install python2 package| image:: https://img.shields.io/github/workflow/status/vroncevic/gen_avr8/gen_avr8_python2_build?style=flat&label=gen_avr8%20python2%20build
   :target: https://img.shields.io/github/workflow/status/vroncevic/gen_avr8/gen_avr8_python2_build

.. |install python3 package| image:: https://img.shields.io/github/workflow/status/vroncevic/gen_avr8/gen_avr8_python3_build?style=flat&label=gen_avr8%20python3%20build
   :target: https://img.shields.io/github/workflow/status/vroncevic/gen_avr8/gen_avr8_python3_build

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/gen_avr8/releases

To install **gen_avr8** 📦 type the following

.. code-block:: bash

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

You can use Docker to create image/container, or You can use pip to install 📦

.. code-block:: bash

    #python2
    pip install gen-avr8
    #python3
    pip3 install gen-avr8

|github docker checker|

.. |github docker checker| image:: https://img.shields.io/github/workflow/status/vroncevic/gen_avr8/gen_avr8_docker_checker?style=flat&label=gen_avr8%20docker%20checker
   :target: https://img.shields.io/github/workflow/status/vroncevic/gen_avr8/gen_avr8_docker_checker

Usage
------

Create AVR8 Project Blink, MCU/FOSC will be selected during generation process

.. code-block:: bash

    python gen_avr8_run.py -g Blink -t app

Dependencies
-------------

**gen_avr8** tool-module requires other modules and libraries

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

Supported mcus
---------------

Current list of supported microcontrollers

.. code-block:: bash

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

Generation flow of project setup
---------------------------------

Base flow of generation process

.. image:: https://raw.githubusercontent.com/vroncevic/gen_avr8/dev/docs/gen_avr8_flow.png

Tool structure
---------------

**gen_avr8** is based on Template mechanism

.. image:: https://raw.githubusercontent.com/vroncevic/gen_avr8/dev/docs/gen_avr8.png

🧰 Generator structure

.. code-block:: bash

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

Copyright and licence
----------------------

|license: gpl v3| |license: apache 2.0|

.. |license: gpl v3| image:: https://img.shields.io/badge/license-gplv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |license: apache 2.0| image:: https://img.shields.io/badge/license-apache%202.0-blue.svg
   :target: https://opensource.org/licenses/apache-2.0

Copyright (C) 2018 by `vroncevic.github.io/gen_avr8 <https://vroncevic.github.io/gen_avr8>`_

**gen_avr8** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

🌎 🌍 🌏 Lets help and support PSF.

|python software foundation|

.. |python software foundation| image:: https://raw.githubusercontent.com/vroncevic/gen_avr8/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|donate|

.. |donate| image:: https://www.paypalobjects.com/en_us/i/btn/btn_donatecc_lg.gif
   :target: https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
