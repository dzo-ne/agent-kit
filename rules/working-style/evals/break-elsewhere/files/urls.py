from text import slug


def post_path(title):
    return f"/posts/{slug(title)}"
