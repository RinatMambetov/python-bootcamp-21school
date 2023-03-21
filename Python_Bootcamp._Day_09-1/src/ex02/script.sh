#!/bin/sh
python3 -m venv venv
. venv/bin/activate
pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 setup.py build
python3 setup.py install

#rm -rf build dist venv cyth.egg-info cyth/c_matrix_mul.c