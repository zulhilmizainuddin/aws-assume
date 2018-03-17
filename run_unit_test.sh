#!/usr/bin/env bash

export PYTHONPATH="$PYTHONPATH:$(pwd)/awsassume:$(pwd)/awsassume/tests"

python3.6 -m unittest discover