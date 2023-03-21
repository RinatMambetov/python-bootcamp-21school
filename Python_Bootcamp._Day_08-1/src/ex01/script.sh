#!/bin/sh
python3 -m venv venv
. venv/bin/activate
pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 server.py

#python crawl.py https://www.google.com https://www.wikipedia.org/404 https://www.example.com https://www.pipsnacks.com/404 https://ya.ru
