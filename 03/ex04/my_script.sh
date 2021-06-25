#!/bin/sh
python3 -m venv django_venv
source django_venv/bin/activate

python3 -m pip3 install --upgrade pip
pip3 install -r requirement.txt
pip3 --version

