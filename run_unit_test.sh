#!/usr/bin/env bash

export PYTHONPATH="$PYTHONPATH:$(pwd)/awsassume:$(pwd)/tests"

#python3.6 -m unittest discover
python3.6 -m pytest -vv