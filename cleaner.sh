#! /bin/bash

sudo -u postgres psql -f cleaner.sql
rm log_*.txt
rm *_keys.json
rm -rf *_files