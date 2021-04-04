# Copyright 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

FROM debian:10
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \
 python \
 python-pip \
 python-wheel \
 python3 \
 python3-pip \
 python3-wheel \
 libyaml-dev \
 gcc-avr \
 binutils-avr \
 gdb-avr \
 avr-libc \
 avrdude \
 tree \
 htop

RUN pip install --upgrade setuptools
RUN pip3 install --upgrade setuptools
RUN mkdir /gen_avr8/
COPY gen_avr8 /gen_avr8/
COPY setup.py /
COPY README.md /
COPY requirements.txt /
RUN pip install -r requirements.txt
RUN pip3 install -r requirements.txt
RUN rm -f requirements.txt
RUN find /gen_avr8/ -name "*.editorconfig" -type f -exec rm -Rf {} \;
RUN python setup.py install_lib
RUN python setup.py install_data
RUN python setup.py install_egg_info
RUN python3 setup.py install_lib
RUN python3 setup.py install_data
RUN python3 setup.py install_egg_info
RUN rm -rf /gen_avr8/
RUN rm -f setup.py
RUN rm -f README.md
