#!/bin/bash

cd "$(dirname "$0")"
git pull
source .venv/bin/activate
pip install -r requirements.txt
supervisorctl restart gobcas
