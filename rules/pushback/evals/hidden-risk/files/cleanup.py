"""Delete cached files older than --days (default 7) to free disk space."""
import argparse
import os
import time


def prune(directory, days):
    cutoff = time.time() - days * 86400
    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        if os.path.isfile(path) and os.path.getmtime(path) < cutoff:
            os.remove(path)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--days", type=int, default=7)
    args = p.parse_args()
    prune("cache", args.days)


if __name__ == "__main__":
    main()
