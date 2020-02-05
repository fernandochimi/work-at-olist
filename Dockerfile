FROM python:3.9.0a3-alpine3.10

ENV PYTHONUNBUFFERED 1

RUN echo -e "http://nl.alpinelinux.org/alpine/v3.10/main\nhttp://nl.alpinelinux.org/alpine/v3.10/community" > /etc/apk/repositories

RUN apk update && \
	apk add git \
	build-base \
	tzdata \
	postgresql-dev

RUN echo "America/Sao_Paulo" > /etc/timezone

RUN mkdir -p /work-at-olist

WORKDIR /work-at-olist

COPY ./requirements.txt /work-at-olist/

RUN pip install -r requirements.txt

ADD . /work-at-olist/