#!/usr/bin/env bash

export PYTHONPATH="$(pwd)/awsassume:$(pwd)/awsassume/tests"

python3 -m mypy --ignore-missing-imports awsassume