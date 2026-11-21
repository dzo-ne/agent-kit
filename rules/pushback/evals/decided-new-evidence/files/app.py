import os

from netutil import parse_host, parse_port


def main():
    host = parse_host(os.environ.get("HOST", "localhost"))
    port = parse_port(os.environ.get("PORT", "8080"))
    print(f"listening on {host}:{port}")


if __name__ == "__main__":
    main()
