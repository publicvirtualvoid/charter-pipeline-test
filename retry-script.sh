#!/bin/bash
# used to test clean env functionality
set -x
# deactivate
rm -rf test-env
python3 -m venv test-env
source test-env/bin/activate
pip install --no-cache-dir -r requirements.txt
pip cache purge
python clean-venv.py test-env > clean_output.txt
python __main__.py 1 2 3 4 5
tar -czf test-env.tar.gz test-env
du -h --max-depth=1
ls -lah