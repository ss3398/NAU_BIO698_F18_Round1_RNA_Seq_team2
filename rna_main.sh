#!/bin/bash

echo Loading S_TABLE
./loadcsv.py

echo Create T_TABLE

mysql -h localhost -u bio698 -pbio698 < ms1.sql

echo Loading T_TABLE

mysqlimport --ignore-lines=1 --fields-terminated-by=, --fields-optionally-enclosed-by='\"' --columns='id,target_id,sample,est_counts,tpm,eff_len,len,resistance_profile,treatment' --local -u bio698 -pbio698 bio698 k_table.csv

echo Summarizing T_TABLE and creating Output.txt

mysql -h localhost -u bio698 -pbio698 < ms2.sql

Moving Output.txt to current directory

mv /var/lib/mysql-files/Output.txt Output.txt 
mv /var/lib/mysql-files/readcounts.txt readcounts.txt 

./box.py

