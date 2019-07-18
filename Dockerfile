FROM python:latest

MAINTAINER Ryan Wong

COPY MaterialsIO /MaterialsIO

RUN pip install stevedore sphinx_rtd_theme \
pymatgen ase mdf_toolbox python-magic dfttopif \
hyperspy hyperspy_gui_ipywidgets hyperspy_gui_traitsui

ENTRYPOINT ["python", "MaterialsIO/cmd_parser_executer.py"]