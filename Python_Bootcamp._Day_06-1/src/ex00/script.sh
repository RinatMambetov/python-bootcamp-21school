#!/bin/sh
python3 -m venv venv
. venv/bin/activate
pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ship.proto
python3 reporting_server.py



#python reporting_client.py 17 45 40.0409 -29 00 28.118
