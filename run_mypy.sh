#!/usr/bin/env bash

export PYTHONPATH="$PYTHONPATH:$(pwd)/awsassume"

python3 -m mypy --ignore-missing-imports awsassume