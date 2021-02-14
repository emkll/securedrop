def test_system_time(host):
    c = host.run("timedatectl show")
    assert "NTP=yes" in c.stdout
    assert "NTPSynchronized=yes" in c.stdout
