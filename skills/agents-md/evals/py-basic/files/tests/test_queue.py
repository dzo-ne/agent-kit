from tinyq import Queue


def test_roundtrip(tmp_path):
    q = Queue(str(tmp_path / "q.db"))
    job = q.put("hello")
    assert q.take() == (job, "hello")
    q.done(job)
    assert q.take() is None
