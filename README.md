# AVR project skeleton generator.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

### INSTALLATION

To install this set of modules type the following:

```
cp -R ~/gen_avr8_scripts/bin/   /root/scripts/gen_avr8/ver.1.0/
cp -R ~/gen_avr8_scripts/conf/  /root/scripts/gen_avr8/ver.1.0/
cp -R ~/gen_avr8_scripts/log/   /root/scripts/gen_avr8/ver.1.0/
```

### DEPENDENCIES

This module requires these other modules and libraries:

* ats_utilities https://vroncevic.github.io/ats_utilities

### Tool structure

![alt tag](https://raw.githubusercontent.com/vroncevic/gen_avr8/dev/python-tool-docs/gen_avr8.png)

```
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
│   └── template
│       ├── Makefile.template
│       ├── module.template
│       ├── objects.template
│       ├── sources.template
│       └── subdir.template
└── log
    └── gen_avr8.log
```

### COPYRIGHT AND LICENCE

Copyright (C) 2019 by https://vroncevic.github.io/gen_avr8/

This tool is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.7/3.4 or,
at your option, any later version of Python 3 you may have available.

:sparkles:
