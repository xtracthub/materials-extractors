FROM ubuntu:latest

FROM python:latest

MAINTAINER Ryan Wong 

RUN git clone https://github.com/materials-data-facility/MaterialsIO.git && cd MaterialsIO && pip install -e .

COPY cmd_parser_executer.py /MaterialsIO

RUN pip install stevedore sphinx_rtd_theme \
pymatgen ase mdf_toolbox python-magic dfttopif \
hyperspy hyperspy_gui_ipywidgets hyperspy_gui_traitsui

ENTRYPOINT ["python", "MaterialsIO/cmd_parser_executer.py"]
