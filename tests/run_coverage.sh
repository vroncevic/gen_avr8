#!/bin/bash
#
# @brief   gen_avr8
# @version v1.0.1
# @date    Sat Aug 11 09:58:41 2018
# @company None, free software to use 2018
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

rm -rf htmlcov gen_avr8_coverage.xml gen_avr8_coverage.json .coverage
rm -rf simple_test/ new_simple_test/ new_pro/ tester/ tester2/
ats_coverage_run.py -n gen_avr8 -p ../README.md
rm -rf simple_test/ new_simple_test/ new_pro/ tester/ tester2/
python3 -m coverage run -m --source=../gen_avr8 unittest discover -s ./ -p '*_test.py' -vvv
python3 -m coverage html -d htmlcov
python3 -m coverage xml -o gen_avr8_coverage.xml 
python3 -m coverage json -o gen_avr8_coverage.json
python3 -m coverage report --format=markdown -m
