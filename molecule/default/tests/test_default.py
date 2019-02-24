import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_os_env_distribution(host):
    assert host.system_info.distribution == 'centos'
    assert '7.6' in host.check_output('cat /etc/redhat-release')


def test_os_env_selinux(host):
    assert 'Disabled' in host.check_output('getenforce')


def test_os_env_timezone(host):
    assert 'Asia/Tokyo' in host.check_output('timedatectl | grep "Time zone:"')


def test_os_env_locale(host):
    assert 'ja_JP.UTF-8' in host.check_output('localectl | grep Locale')


def test_os_env_kernel_parameters(host):
    assert 1 == host.sysctl('net.ipv6.conf.all.disable_ipv6')
    assert 1 == host.sysctl('net.ipv6.conf.default.disable_ipv6')
    assert 1 == host.sysctl('net.ipv4.tcp_syncookies')
    assert 1 == host.sysctl('net.ipv4.icmp_echo_ignore_broadcasts')


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


def test_os_firewalld_is_installed(host):
    package = host.package('firewalld')
    assert package.is_installed


def test_os_firewalld_running_and_enabled(host):
    service = host.service('firewalld')
    assert service.is_running
    assert service.is_enabled


def test_os_firewalld_rules(host):
    cmd = 'iptables -L INPUT_direct | grep '
    rule1 = cmd + '"tcp flags:FIN,SYN,RST,PSH,ACK,URG/NONE"'
    rule2 = cmd + '"tcp flags:!FIN,SYN,RST,ACK/SYN state NEW"'
    rule3 = cmd + '"tcp flags:FIN,SYN,RST,PSH,ACK,URG/FIN,SYN,RST,PSH,ACK,URG"'
    assert 0 == host.run(rule1).rc
    assert 0 == host.run(rule2).rc
    assert 0 == host.run(rule3).rc
