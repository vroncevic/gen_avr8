# Copyright 2019 Vladimir Roncevic <elektron.ronca@gmail.com>
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
 gcc-avr \
 binutils-avr \
 gdb-avr \
 avr-libc \
 avrdude \
 tree

# Install dependency
RUN pip install --upgrade setuptools
RUN mkdir /gen_avr8/
COPY gen_avr8 /gen_avr8/
COPY setup.py /
COPY requirements.txt /
RUN pip install -r requirements.txt
RUN rm -f requirements.txt
RUN find /gen_avr8/ -name "*.editorconfig" -type f -exec rm -Rf {} \;
RUN python setup.py install_lib && python setup.py install_data && python setup.py install_egg_info
RUN rm -rf /gen_avr8/
RUN rm -f setup.py
RUN chmod -R 755 /usr/local/lib/python2.7/dist-packages/gen_avr8/
RUN chmod -R 644 /usr/local/lib/python2.7/dist-packages/gen_avr8-1.1.0.egg-info/
RUN tree /usr/local/lib/python2.7/dist-packages/gen_avr8/
RUN ln -s /usr/local/bin/gen_avr8_run.py /usr/bin/gen_avr8
