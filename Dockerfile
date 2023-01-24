FROM python:3.10.2

ENV PYTHONUNBUFFERED 1

WORKDIR /adi

ADD requirements.txt /adi/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# ① Install some dependencies
RUN apt-get update \
    && apt-get install -y libsasl2-dev python-dev libldap2-dev libssl-dev \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean


# Copy adi
ADD /adi /adi


VOLUME /usr/src