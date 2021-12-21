FROM python:3.6

MAINTAINER Globus Labs, University of Chicago (Ryan Wong rewong03@gmail.com; Tyler Skluzacek skluzacek@uchicago.edu) 

RUN pip install --upgrade pip

RUN git clone https://github.com/materials-data-facility/MaterialsIO.git \
    && cd MaterialsIO && pip install -e . \
    && cd
    #&& pip install -r requirements.txt \
    #&& cd

COPY mdf-materialsio-adapters /mdf-materialsio-adapters
RUN cd /mdf-materialsio-adapters && pip install -e . && cd

COPY data-schemas /data-schemas

# Get the Xtract code here so we have access to exceptions. 
RUN git clone https://github.com/xtracthub/xtracthub-service.git \ 
    && cp xtracthub-service/exceptions.py /

RUN pip install xtract_sdk==0.0.7a3
RUN pip install funcx
RUN pip install funcx_endpoint


ENV CONTAINER_VERSION=1.0

COPY xtract_matio_main.py / 
RUN pip install xtract-sdk

RUN pip uninstall globus_sdk -y && pip install globus_sdk==2.0.1

RUN pip install ase dfttopif python-magic sphinx_rtd_theme tableschema xmltodict

COPY test_file.py /

