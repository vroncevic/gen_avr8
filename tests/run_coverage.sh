#!/bin/bash
#
# @brief   gen_avr8
# @version v1.0.1
# @date    Sat Aug 11 09:58:41 2018
# @company None, free software to use 2018
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 -m coverage run -m --source=../gen_avr8 unittest discover -s ./ -p '*_test.py'
python3 -m coverage html
