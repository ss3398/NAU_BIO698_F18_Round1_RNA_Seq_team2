#!/bin/bash

rm Output.txt

mysql -h localhost -u bio698 -pbio698 < clean.sql

