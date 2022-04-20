import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_os_env_distribution(host):
    assert host.system_info.distribution == 'centos'
    assert '7.9' in host.check_output('cat /etc/redhat-release')


def test_os_env_selinux(host):
    cmd = host.run('getenforce')
    assert 0 == cmd.rc
    assert 'Enforcing' != cmd.stdout


def test_os_yum_update(host):
    cmd = host.run('yum check-update')
    assert 0 == cmd.rc


def test_os_add_package_is_installed(host):
    package = host.package('bash-completion')
    assert package.is_installed


def test_os_env_timezone(host):
    assert 'Asia/Tokyo' in host.check_output('timedatectl | grep "Time zone:"')


def test_os_env_locale(host):
    assert 'ja_JP.UTF-8' in host.check_output('localectl | grep Locale')


def test_os_ntp_is_installed(host):
    package = host.package('chrony')
    assert package.is_installed


def test_os_ntp_running_and_enabled(host):
    service = host.service('chronyd')
    assert service.is_running
    assert service.is_enabled


def test_os_ntp_is_listen(host):
    assert host.socket('udp://0.0.0.0:123').is_listening


def test_os_sshd_is_installed(host):
    package = host.package('openssh-server')
    assert package.is_installed


def test_os_sshd_running_and_enabled(host):
    service = host.service('sshd')
    assert service.is_running
    assert service.is_enabled


def test_os_sshd_is_listen(host):
    assert host.socket('tcp://0.0.0.0:22').is_listening
