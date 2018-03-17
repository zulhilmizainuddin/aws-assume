#!/usr/bin/env bash

export PYTHONPATH="$(pwd)/awsassume:$(pwd)/awsassume/tests"

python3.6 -m unittest discover