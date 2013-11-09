import os


def path(path):
    this_dir = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(this_dir, "../test-files", path)
