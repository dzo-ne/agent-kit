import os, sys
import re


def ParseLine(l):
    x = l.split(",")
    if len(x) != 3:
        raise ValueError("expected 3 feilds, got %d" % len(x))
    return x
