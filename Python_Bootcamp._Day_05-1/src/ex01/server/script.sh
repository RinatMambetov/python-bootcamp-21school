#!/bin/sh
python3 -m venv venv
. venv/bin/activate
pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 server.py
