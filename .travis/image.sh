#!/bin/bash
for i in centos-molecule:7
do
    docker pull paulfantom/$i &
done

wait
