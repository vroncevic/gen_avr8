AVR project skeleton generator
===============================

**gen_avr8** is toolset for generation of AVR8 project skeleton for
development embedded applications.

Developed in `python <https://www.python.org/>`_ code: **100%**.

The README is used to introduce the tool modules and provide instructions on
how to install the tool modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|Python package| |GitHub issues| |Documentation Status| |GitHub contributors|

.. |Python package| image:: https://github.com/vroncevic/gen_avr8/workflows/Python%20package/badge.svg
   :target: https://github.com/vroncevic/gen_avr8/workflows/Python%20package/badge.svg?branch=master

.. |GitHub issues| image:: https://img.shields.io/github/issues/vroncevic/gen_avr8.svg
   :target: https://github.com/vroncevic/gen_avr8/issues

.. |GitHub contributors| image:: https://img.shields.io/github/contributors/vroncevic/gen_avr8.svg
   :target: https://github.com/vroncevic/gen_avr8/graphs/contributors

.. |Documentation Status| image:: https://readthedocs.org/projects/gen_avr8/badge/?version=latest
   :target: https://gen_avr8.readthedocs.io/projects/gen_avr8/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents:

   modules
   self

Installation
-------------

|Install Python2 Package| |Install Python3 Package|

.. |Install Python2 Package| image:: https://github.com/vroncevic/gen_avr8/workflows/Install%20Python2%20Package%20gen_avr8/badge.svg
   :target: https://github.com/vroncevic/gen_avr8/workflows/Install%20Python2%20Package%20gen_avr8/badge.svg?branch=master

.. |Install Python3 Package| image:: https://github.com/vroncevic/gen_avr8/workflows/Install%20Python3%20Package%20gen_avr8/badge.svg
   :target: https://github.com/vroncevic/gen_avr8/workflows/Install%20Python3%20Package%20gen_avr8/badge.svg?branch=master

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/gen_avr8/releases

To install **gen_avr8** type the following:

.. code-block:: bash

    tar xvzf gen_avr8-x.y.z.tar.gz
    cd gen_avr8-x.y.z/
    python setup.py install_lib
    python setup.py install_data
    python setup.py install_egg_info

You can use Docker to create image/container.

|GitHub docker checker|

.. |GitHub docker checker| image:: https://github.com/vroncevic/gen_avr8/workflows/gen_avr8%20docker%20checker/badge.svg
   :target: https://github.com/vroncevic/gen_avr8/actions?query=workflow%3A%22gen_avr8+docker+checker%22

Usage
------

Create AVR8 Project Blink, MCU/FOSC will be selected during generation process:

.. code-block:: bash

    python gen_avr8_run -g Blink


Crete AVR8 Project Blink, by using parameters from yaml file:

.. code-block:: bash

    python gen_avr8_run -g Blink -c avr8.yaml


Content of configuration file avr8.yaml:

.. code-block:: bash

    cat avr8.yaml
    MCU:
        atmega8
    OSC:
        16000000UL

Dependencies
-------------

**gen_avr8** tool-module requires other modules and libraries:
    sh_util `https://github.com/vroncevic/sh_util <https://github.com/vroncevic/sh_util>`_

Supported mcus
---------------

Current list of supported microcontrollers:

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

Base flow of generation process:

.. image:: https://raw.githubusercontent.com/vroncevic/gen_avr8/dev/docs/gen_avr8_flow.png

Tool structure
---------------

**gen_avr8** is based on Template mechanism:

.. image:: https://raw.githubusercontent.com/vroncevic/gen_avr8/dev/docs/gen_avr8.png

Generator structure:

.. code-block:: bash

    gen_avr8_run.py
    │
    ├── conf/
    │   ├── fosc.yaml
    │   ├── gen_avr8.cfg
    │   ├── gen_avr8_util.cfg
    │   ├── mcu.yaml
    │   ├── project.yaml
    │   └── template/
    │       ├── cflags.template
    │       ├── csflags.template
    │       ├── Makefile.template
    │       ├── module.template
    │       ├── objects.template
    │       ├── ocflags.template
    │       ├── odflags.template
    │       ├── sources.template
    │       └── subdir.template
    │
    ├── gen_avr8/
    │   ├── avr8_pro/
    │   │   ├── avr8_setup.py
    │   │   ├── __init__.py
    │   │   ├── mcu_selector.py
    │   │   ├── osc_selector.py
    │   │   ├── read_template.py
    │   │   └── write_template.py
    │   └── __init__.py
    │
    └── log/
        └── gen_avr8.log

Copyright and licence
----------------------

|License: GPL v3| |License: Apache 2.0|

.. |License: GPL v3| image:: https://img.shields.io/badge/License-GPLv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |License: Apache 2.0| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
   :target: https://opensource.org/licenses/Apache-2.0

Copyright (C) 2019 by `vroncevic.github.io/gen_avr8 <https://vroncevic.github.io/gen_avr8>`_

**gen_avr8** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|Python Software Foundation|

.. |Python Software Foundation| image:: https://raw.githubusercontent.com/vroncevic/gen_avr8/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|Donate|

.. |Donate| image:: https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif
   :target: https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
