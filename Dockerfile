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
RUN DEBIAN_FRONTEND=noninteractive \
    apt-get install -yq --no-install-recommends \
    tree \
    htop \
    wget \
    unzip \
    ca-certificates \
    openssl \
    libyaml-dev \
    python \
    python-dev \
    python-wheel \
    python3 \
    python3-wheel \
    python3-venv \
    python3-dev \
    gcc-avr \
    binutils-avr \
    gdb-avr \
    avr-libc \
    avrdude

RUN wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
RUN python2 get-pip.py
RUN python2 -m pip install --upgrade setuptools
RUN python2 -m pip install --upgrade pip
RUN python2 -m pip install --upgrade build
RUN rm -f get-pip.py
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py
RUN python3 -m pip install --upgrade setuptools
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade build
RUN rm -f get-pip.py
COPY requirements.txt /
RUN python3 -m venv env
RUN mkdir /gen_avr8/
COPY gen_avr8 /gen_avr8/
COPY setup.cfg /
COPY pyproject.toml /
COPY MANIFEST.in /
COPY setup.py /
COPY README.md /
COPY LICENSE /
RUN pip2 install -r requirements.txt
RUN pip3 install -r requirements.txt
RUN rm -f requirements.txt
RUN find /gen_avr8/ -name "*.editorconfig" -type f -exec rm -Rf {} \;
RUN python2 -m build --no-isolation --wheel
RUN pip2 install /dist/gen_avr8-*-py2-none-any.whl
RUN python3 -m build --no-isolation --wheel
RUN pip3 install /dist/gen_avr8-*-py3-none-any.whl
RUN rm -rf /gen_avr8/
RUN rm -f setup.py
RUN rm -f README.md
RUN rm -f setup.cfg
RUN rm -f pyproject.toml
RUN rm -f MANIFEST.in
RUN rm -f LICENSE
