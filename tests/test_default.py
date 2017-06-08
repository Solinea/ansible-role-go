import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_go_executable_installed(host):
    assert host.file("/usr/local/go/bin/go").exists
