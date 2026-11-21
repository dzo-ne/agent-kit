import os

UPLOADS = "uploads"


def save_upload(name, data):
    with open(os.path.join(UPLOADS, name), "wb") as f:
        f.write(data)
