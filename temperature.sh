#!/bin/bash
cd /home/pi/temperature
source env/bin/activate
export PYTHONPATH=/home/pi/temperature:
python temperature.py >> temp.log
