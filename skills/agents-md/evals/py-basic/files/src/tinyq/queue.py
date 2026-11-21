"""Public queue API built on Store."""
from .store import Store


class Queue:
    def __init__(self, path: str = "tinyq.db"):
        self.store = Store(path)

    def put(self, body: str) -> int:
        return self.store.add(body)

    def take(self):
        return self.store.next()

    def done(self, job_id: int) -> None:
        self.store.finish(job_id)
