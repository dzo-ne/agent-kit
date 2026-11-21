"""Helpers for text you recieve from the API."""


def shout(s):
    return s.upper() + "!"


def initials(name):
    return "".join(part[0] for part in name.split())
