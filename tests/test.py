# -*- coding:utf8 -*-

def test_os_info_distribution(host):
    assert host.system_info.distribution == "centos"
    assert "7.6" in host.run("cat /etc/redhat-release").stdout

def test_os_info_selinux(host):
    assert "Disabled" in host.run("getenforce").stdout

def test_os_env_timezone(host):
    assert "Asia/Tokyo" in host.run("timedatectl | grep 'Time zone:'").stdout

def test_os_env_locale(host):
    assert "ja_JP.UTF-8" in host.run("localectl | grep Locale").stdout
