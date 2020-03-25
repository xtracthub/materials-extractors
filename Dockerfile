FROM python:3.6

MAINTAINER Globus Labs, University of Chicago (Ryan Wong rewong03@gmail.com; Tyler Skluzacek skluzacek@uchicago.edu) 

RUN git clone https://github.com/materials-data-facility/MaterialsIO.git \
    && cd MaterialsIO && pip install -e . \
    && pip install -r requirements.txt \
    && cd
    

ENV container_version=5


COPY xtract_matio_main.py / 
