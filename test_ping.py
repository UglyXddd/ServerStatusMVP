import subprocess

import ping_file

def test_ping_func_returns_online(monkeypatch):
    class MockResult:
        returncode = 0

        def mock_run(*args, **kwargs):
            return MockResult()

        monkeypatch.setattr(subprocess, "run", mock_run)

        assert ping_file.ping_func("127.0.0.1") == "✅"


def test_ping_func_returns_offline(monkeypatch):
    class MockResult:
        returncode = 1

        def mock_run(*args, **kwargs):
            return MockResult()

        monkeypatch.setattr(subprocess, "run", mock_run)

        assert ping_file.ping_func("192.0.2.1") == "🔴"


def test_ping_range_checks_all_hosts(monkeypatch):
    checked_hosts = []

    def mock_ping(host):
        checked_hosts.append(host)
        return "✅"

    monkeypatch.setattr(ping_file, "ping_func", mock_ping)

    result = ping_file.ping_range(
        ["192.0.2.1", "192.0.2.2", "192.0.2.3"]
    )

    assert result == ["✅", "✅", "✅"]
    assert checked_hosts == [
        "192.0.2.1",
        "192.0.2.2",
        "192.0.2.3",
    ]

