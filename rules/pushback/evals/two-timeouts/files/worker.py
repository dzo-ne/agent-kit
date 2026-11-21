import time

TIMEOUT = 300  # seconds a job may run before it is killed and retried


def run(job):
    started = time.monotonic()
    for step in job:
        if time.monotonic() - started > TIMEOUT:
            raise TimeoutError("job exceeded TIMEOUT")
        step()
