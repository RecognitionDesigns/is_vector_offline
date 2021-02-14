#!/bin/bash

while :
do
    if ping -c 5 -W 1 "192.168.0.15"; then
      cd ~/VectorSdk/ && sudo rmdir alert_run_once
      sleep 300
    else
      python3 ./vector_alert_no_connection.py
      sleep 300
    fi
done