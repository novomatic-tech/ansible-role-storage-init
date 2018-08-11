Role Name
=========

Simple role to initialize lvm volumes on host. This role was created to automate machines bootstrapping.

Default Behavior
-----------------
Please check [config.yml](./tasks/config.yml)

Designing defaults:
 * Scanning SCSI bus to find new devices (used default bus 0-7).
 * Resizing existing LVM physical volumes.
 * Resizing file system.

Role Variables
--------------
All variables persent here: [main.yml](./defaults/main.yml).


Example Playbook
----------------
```
- hosts: test_group
  vars:
    lvm_vgs:
     - name: extra
       disks:
       - /dev/vdb
       - /dev/vdc

    lvm_volumes:
     - name: docker
       vg: extra
       size: 3G
       fstype: xfs
       path: "/var/lib/docker"
       opts: "-n ftype=1"
     - name: test
       vg: extra
       size: 2G
       fstype: ext4
       path: "/var/lib/test"
  roles:
    - novomatic-tech/storage-init
```
 License
 -------

 MIT


Author Information
------------------

This role was created in 2018 for Novomatic Technologies Poland purposes.
