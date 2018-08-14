#!/bin/bash
dd if=/dev/zero of=lvmtest0.img bs=200 count=1M
sudo losetup /dev/loop0 lvmtest0.img
for i in centos-molecule:7
do
    docker pull paulfantom/$i &
done

wait
