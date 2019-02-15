# -*- coding:utf8 -*-

def test_[template]_is_installed(host):
    [template] = host.package("[template]")
    assert [template].is_installed
    assert [template].version.startswith("[version]")

def test_[template]_running_and_enabled(host):
    [template] = host.service("[template]")
    assert [template].is_running
    assert [template].is_enabled

def test_[template]_is_listen(host):
    assert host.socket("tcp://0.0.0.0:[port]").is_listening
