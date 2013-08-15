#!/bin/sh

ls -l --human
ls -l --human |  awk '{T+=$5} END {print "Size of files:"T}'
