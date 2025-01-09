#!/bin/sh
echo "copy files"
ls -al ../../../lib
cp ../../../lib/util.py .
cp ../../../lib/dynamodb.py .
ls -al .
