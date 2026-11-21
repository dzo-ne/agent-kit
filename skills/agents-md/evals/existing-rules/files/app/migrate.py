"""Apply db/migrations/NNN_*.sql in order. Applied files are recorded by name,
so editing one after it ran has no effect on existing databases."""
import pathlib
import sqlite3


def main(db: str = "ledger.db") -> None:
    conn = sqlite3.connect(db)
    conn.execute("CREATE TABLE IF NOT EXISTS applied (name TEXT PRIMARY KEY)")
    done = {r[0] for r in conn.execute("SELECT name FROM applied")}
    for f in sorted(pathlib.Path("db/migrations").glob("*.sql")):
        if f.name not in done:
            conn.executescript(f.read_text())
            conn.execute("INSERT INTO applied VALUES (?)", (f.name,))
    conn.commit()


if __name__ == "__main__":
    main()
