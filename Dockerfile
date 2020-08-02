FROM ubuntu:latest

ARG DEBIAN_FRONTEND=noninteractive
ENV QT_QPA_PLATFORM=offscreen

RUN apt-get update && apt-get install -y musescore3

RUN apt-get update && apt-get install -y python3 python3-pip

WORKDIR /usr/src/app

RUN pip3 install --upgrade pip
COPY requirements.txt /usr/src/app/requirements.txt
RUN pip3 install -r requirements.txt
