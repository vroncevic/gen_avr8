#!/bin/bash
#
# @brief   gen_avr8
# @version 2.6.6
# @date    Sun Jun 30 09:25:12 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 main.py create --name "atsystem" --type "app" --output "./demo_app"

python3 main.py create --name "atsystem" --type "lib" --output "./demo_lib"
