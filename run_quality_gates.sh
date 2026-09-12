#!/bin/bash
#
# @brief   gen_avr8
# @version 2.6.6
# @date    Sun Jun 30 09:25:12 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 gates/gates/interfaces_checker.py gen_avr8
python3 gates/gates/isp_checker.py gen_avr8
python3 gates/gates/limits_checker.py gen_avr8
python3 gates/gates/srp_checker.py gen_avr8

echo "Done"
