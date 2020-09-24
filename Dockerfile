FROM ubuntu:18.04

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
    curl apt-utils apt-transport-https \
    git \
    python3.7 \
    python3-dev \
    python3-setuptools \
    python3-pip \
    nginx \
    supervisor \
    sqlite3 &&\
    rm -rf /var/lib/apt/lists/*

RUN pip3 install -U pip setuptools
RUN apt-get install python3-setuptools

ADD requirements.txt /project/

RUN pip3 install -r /project/requirements.txt

ADD . /project/

COPY deployments/nginx_inside_kids /etc/nginx/sites-available/default
COPY deployments/supervisord.conf /etc/supervisor/conf.d/

EXPOSE 80
EXPOSE 443

CMD ["supervisord", "-n"]