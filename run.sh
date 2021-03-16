#!/bin/sh
echo "Starting Vaico-Demo"
echo "Running Dashboard"
./venv/bin/python -m VaicoDemo.dashboard &
echo "Running Detector"
./venv/bin/python -m VaicoDemo.start