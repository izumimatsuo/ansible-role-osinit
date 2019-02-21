import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_os_info_distribution(host):
    assert host.system_info.distribution == "centos"
    assert "7.6" in host.run("cat /etc/redhat-release").stdout


def test_os_env_selinux(host):
    assert "Disabled" in host.run("getenforce").stdout


def test_os_env_timezone(host):
    assert "Asia/Tokyo" in host.run("timedatectl | grep 'Time zone:'").stdout


def test_os_env_locale(host):
    assert "ja_JP.UTF-8" in host.run("localectl | grep Locale").stdout


def test_chrony_is_installed(host):
    chrony = host.package("chrony")
    assert chrony.is_installed


def test_chrony_running_and_enabled(host):
    chrony = host.service("chronyd")
    assert chrony.is_running
    assert chrony.is_enabled


def test_chrony_is_listen(host):
    assert host.socket("tcp://0.0.0.0:123").is_listening
