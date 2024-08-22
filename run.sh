#!/bin/bash

cd "$(dirname "$0")"
source .venv/bin/activate
exec gunicorn -c gunicorn.conf.py main:app
