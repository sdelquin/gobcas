#!/bin/bash

source ~/.virtualenvs/gobcas/bin/activate
cd "$(dirname "$0")"
exec gunicorn -c gunicorn.conf.py main:app
