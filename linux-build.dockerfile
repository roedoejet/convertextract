FROM debian:buster-slim

COPY . /src

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git

RUN pip3 install -U -f \
    https://extras.wxpython.org/wxPython4/extras/linux/gtk3/debian-10/wxPython-4.1.0-cp37-cp37m-linux_x86_64.whl wxPython4

RUN pip3 install -r /src/requirements.txt

RUN pip3 install git+https://github.com/roedoejet/Gooey.git pyinstaller

RUN cd /src && pyinstaller build.spec