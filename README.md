[![Build Status](https://travis-ci.org/novomatic-tech/ansible-role-storage-init.svg?branch=master)](https://travis-ci.org/novomatic-tech/ansible-role-storage-init) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![Ansible Role Name](https://img.shields.io/ansible/role/28820.svg)](https://galaxy.ansible.com/novomatic-tech/storage_init/) [![Ansible Role counter](https://img.shields.io/ansible/role/d/28820.svg)](https://galaxy.ansible.com/novomatic-tech/storage_init/)

Ansible-role-storage-init
=========

Simple role to initialize LVM volumes on host. This role was created to automate machines bootstrapping. Role is dedicated to initial setup of LVM and increase existing volumes or fs.

If something is missing please create a issue on [github](https://github.com/novomatic-tech/ansible-role-storage-init)

Default Behavior
-----------------
Please check [config.yml](./tasks/config.yml)

Designing defaults:
 * Scanning SCSI bus to find new devices (used default bus 0-7).
 * Resizing existing LVM physical volumes.
 * Resizing file system.

*Shrinking operation is not support by the file system module and we do not plan to add some extra logic for it.*

Role Variables
--------------
All variables present here: [main.yml](./defaults/main.yml).


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
