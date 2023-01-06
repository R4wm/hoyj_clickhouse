#!/bin/bash
for i in $(docker container ls | grep -v CONTAINER | awk {'print $1'}); do docker container rm -f $i; done
