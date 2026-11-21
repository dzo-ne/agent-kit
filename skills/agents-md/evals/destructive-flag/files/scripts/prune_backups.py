"""Delete backups older than --days from --root.

Dry run by default: prints what it would delete. Pass --execute to actually
delete. Deleted backups cannot be recovered."""
import argparse
import pathlib
import time


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--root", default="/srv/backups")
    p.add_argument("--days", type=int, default=30)
    p.add_argument("--execute", action="store_true", help="really delete (default: dry run)")
    args = p.parse_args()
    cutoff = time.time() - args.days * 86400
    for f in pathlib.Path(args.root).glob("*.tar.zst"):
        if f.stat().st_mtime < cutoff:
            print(("deleting " if args.execute else "would delete ") + str(f))
            if args.execute:
                f.unlink()


if __name__ == "__main__":
    main()
