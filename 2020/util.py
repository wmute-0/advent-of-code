"""
Utility functions that help with routine tasks
"""

def read_text_lines(path):
    with open(path, "r") as infile:
        return infile.read().splitlines()


def read_int_lines(path):
    with open(path, "r") as infile:
        lns = infile.readlines()
        return [int(x) for x in lns.strip()]