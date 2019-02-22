import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_os_info_distribution(host):
    assert host.system_info.distribution == "centos"
    assert "7.6" in host.check_output("cat /etc/redhat-release")


def test_os_env_selinux(host):
    assert "Disabled" in host.check_output("getenforce")


def test_os_env_timezone(host):
    assert "Asia/Tokyo" in host.check_output("timedatectl | grep 'Time zone:'")


def test_os_env_locale(host):
    assert "ja_JP.UTF-8" in host.check_output("localectl | grep Locale")


def test_chrony_is_installed(host):
    chrony = host.package("chrony")
    assert chrony.is_installed


def test_chrony_running_and_enabled(host):
    chrony = host.service("chronyd")
    assert chrony.is_running
    assert chrony.is_enabled


def test_chrony_is_listen(host):
    assert host.socket("udp://0.0.0.0:123").is_listening


def test_sshd_is_installed(host):
    sshd = host.package("openssh-server")
    assert sshd.is_installed


def test_sshd_running_and_enabled(host):
    sshd = host.service("sshd")
    assert sshd.is_running
    assert sshd.is_enabled


def test_sshd_is_listen(host):
    assert host.socket("tcp://0.0.0.0:22").is_listening


def test_firewalld_is_installed(host):
    firewalld = host.package("firewalld")
    assert firewalld.is_installed


def test_firewalld_running_and_enabled(host):
    firewalld = host.service("firewalld")
    assert firewalld.is_running
    assert firewalld.is_enabled
