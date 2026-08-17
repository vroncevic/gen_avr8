#!/bin/bash
#
# @brief   gen_avr8
# @version 2.6.5
# @date    Sun Jun 30 09:25:12 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 coverage/ats_coverage.py gen_avr8
pylint gen_avr8 > gen_avr8.report
echo "Done"
