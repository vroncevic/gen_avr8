AVR project skeleton generator.
=========================================

gen_avr8 is toolset for generation of AVR8 project skeleton for
development embedded applications.

Developed in python code: 100%.

The README is used to introduce the tool modules and provide instructions on
how to install the tool modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

INSTALLATION
-----------------------------
Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/gen_avr8/releases

To install this set of modules type the following:

tar xvzf gen_avr8-x.y.z.tar.gz
cd gen_avr8-x.y.z/python-tool
cp -R ~/bin/   /root/scripts/gen_avr8/
cp -R ~/conf/  /root/scripts/gen_avr8/
cp -R ~/log/   /root/scripts/gen_avr8/

USAGE
-----------------------------
# Create AVR8 Project Blink, MCU/FOSC will be selected during generation process

python gen_avr8_run -g Blink

# Crete AVR8 Project Blink, by using parameters from yaml file

python gen_avr8_run -g Blink -c avr8.yaml

# Content of configuration file avr8.yaml

cat avr8.yaml

MCU:
    atmega8

OSC:
    16000000UL

DEPENDENCIES
-----------------------------
gen_avr8 tool-module requires other modules and libraries:

* ats_utilities https://vroncevic.github.io/ats_utilities

SUPPORTED MCUS
-----------------------------
Current list of supported microcontrollers:

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

GENERATION FLOW OF PROJECT SETUP
-----------------------------
Base flow of generation process:

![alt tag](https://raw.githubusercontent.com/vroncevic/gen_avr8/dev/docs/gen_avr8_flow.png)

TOOL STRUCTURE
-----------------------------
gen_avr8 is based on Template mechanism:

![alt tag](https://raw.githubusercontent.com/vroncevic/gen_avr8/dev/docs/gen_avr8.png)

Generator structure:

.
├── bin
│   ├── avr8_pro
│   │   ├── avr8_setup.py
│   │   ├── __init__.py
│   │   ├── mcu_selector.py
│   │   ├── osc_selector.py
│   │   ├── read_template.py
│   │   └── write_template.py
│   ├── gen_avr8.py
│   └── gen_avr8_run.py
├── conf
│   ├── fosc.yaml
│   ├── gen_avr8.cfg
│   ├── gen_avr8_util.cfg
│   ├── mcu.yaml
│   ├── project.yaml
│   └── template
│       ├── cflags.template
│       ├── csflags.template
│       ├── Makefile.template
│       ├── module.template
│       ├── objects.template
│       ├── ocflags.template
│       ├── odflags.template
│       ├── sources.template
│       └── subdir.template
└── log
    └── gen_avr8.log

COPYRIGHT AND LICENCE
-----------------------------

Copyright (C) 2019 by https://vroncevic.github.io/gen_avr8/

This tool is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.
