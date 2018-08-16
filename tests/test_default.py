import pytest
from testinfra.utils.ansible_runner import AnsibleRunner
testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


@pytest.mark.parametrize("dirs", [
    "/var/lib/docker",
    "/var/lib/test2"
])
def test_directories(host, dirs):
    d = host.file(dirs)
    assert d.is_directory
    assert d.exists


@pytest.mark.parametrize("mounts", [
    "/var/lib/docker",
    "/var/lib/test2"
])
def test_mounts(host, mounts):
    m = host.mount_point(mounts)
    assert m.exists
    assert m.filesystem == 'xfs'
