FROM alpine:latest

LABEL maintainer="Khiem Doan <doankhiem.crazy@gmail.com>"

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

EXPOSE 8000

WORKDIR /src
COPY service.py .

# use for debug
ENV FLASK_APP service.py
ENV FLASK_DEBUG 1

# install dependences
COPY requirements.txt /src/requirements.txt
RUN apk --no-cache add gcc g++ gfortran python3 python3-dev musl-dev openblas-dev \
    && pip3 install Cython --no-cache-dir \
    && pip3 install -r /src/requirements.txt --no-cache-dir \
    && pip3 install gunicorn gevent --no-cache-dir \
    && rm -rf /var/cache/apk/* \
    && underthesea data

ENTRYPOINT gunicorn service:app \
    --bind=0.0.0.0:8000 --workers=1 --worker-class=gevent
