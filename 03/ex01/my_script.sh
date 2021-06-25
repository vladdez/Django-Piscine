#!/bin/sh

mkdir local_lib
python3 -m pip install --target=local_lib git+https://github.com/jaraco/path --log my_log.log --upgrade --force-reinstall 
pip --version
python3 my_program.py
