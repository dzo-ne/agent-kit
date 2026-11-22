def serialize(post):
    """Render a post's tags as a comma-separated string, without duplicates."""
    tags = set(post["tags"])
    return ",".join(tags)
