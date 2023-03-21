#!/bin/sh
python3 setup.py build
python3 setup.py install
python3 test.py
