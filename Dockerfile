FROM ubuntu:20.04

ENV TZ=America/Los_Angeles
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update -y && \
    apt-get install -y \
    python3 \
    python3-dev \
    python3-pip \
    build-essential \
    autoconf \
    libtool \
    pkg-config \
    wget

COPY ./requirements.txt /c2_app/requirements.txt

WORKDIR /c2_app

RUN pip3 install -r requirements.txt

COPY ./implant.py /c2_app/implant.py

CMD [ "python3", "implant.py" ]