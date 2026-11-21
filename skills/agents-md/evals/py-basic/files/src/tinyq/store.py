"""SQLite storage. This is the only module that opens the database file;
everything else goes through Store so writes stay in one transaction path."""
import sqlite3


class Store:
    def __init__(self, path: str):
        self.conn = sqlite3.connect(path)
        self.conn.execute("CREATE TABLE IF NOT EXISTS jobs (id INTEGER PRIMARY KEY, body TEXT, done INTEGER DEFAULT 0)")

    def add(self, body: str) -> int:
        with self.conn:
            return self.conn.execute("INSERT INTO jobs (body) VALUES (?)", (body,)).lastrowid

    def next(self):
        return self.conn.execute("SELECT id, body FROM jobs WHERE done = 0 ORDER BY id LIMIT 1").fetchone()

    def finish(self, job_id: int) -> None:
        with self.conn:
            self.conn.execute("UPDATE jobs SET done = 1 WHERE id = ?", (job_id,))
