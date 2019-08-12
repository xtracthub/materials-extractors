FROM python:3.6

MAINTAINER Ryan Wong 

RUN git clone https://github.com/materials-data-facility/MaterialsIO.git && cd MaterialsIO && pip install -r requirements.txt

COPY cmd_parser_executer.py /MaterialsIO

RUN pip install git+https://github.com/Parsl/parsl git+https://github.com/DLHub-Argonne/home_run

#ENTRYPOINT ["python", "MaterialsIO/cmd_parser_executer.py"]
