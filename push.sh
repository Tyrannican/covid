#!/bin/bash

python ./covid.py scottish_cases.csv
git add . && git commit -m "Updated Scottish cases $(date +'%d/%m/%y')" && git push origin master

