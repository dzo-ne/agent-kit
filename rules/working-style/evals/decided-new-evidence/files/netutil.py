def parse_host(s):
    assert s, "host must not be empty"
    return s.strip().lower()


def parse_port(s):
    return int(s)
