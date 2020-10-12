FROM python:3.6

MAINTAINER Globus Labs, University of Chicago (Ryan Wong rewong03@gmail.com; Tyler Skluzacek skluzacek@uchicago.edu) 

RUN git clone https://github.com/materials-data-facility/MaterialsIO.git \
    && cd MaterialsIO && pip install -e . \
    && pip install -r requirements.txt \
    && cd

RUN git clone https://github.com/materials-data-facility/mdf-materialsio-adapters.git \
    && cd mdf-materialsio-adapters && pip install -e . \
    && pip install -r requirements.txt \
    && cd

# Get the Xtract code here so we have access to exceptions. 
RUN git clone https://github.com/xtracthub/xtracthub-service.git \ 
    && cp xtracthub-service/exceptions.py /

RUN pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
RUN pip install xtract_sdk==0.0.4a

# RUN pip install parsl==0.9.0

ENV container_version=15

COPY xtract_matio_main.py / 
COPY test_file.py /
