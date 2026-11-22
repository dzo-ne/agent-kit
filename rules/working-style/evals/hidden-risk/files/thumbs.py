import os
import shutil

from storage import UPLOADS

CACHE = "cache"


def thumbnail(name):
    """Return the cached thumbnail path, regenerating it from the upload if missing."""
    path = os.path.join(CACHE, name)
    if not os.path.exists(path):
        shutil.copyfile(os.path.join(UPLOADS, name), path)  # stand-in for resizing
    return path
