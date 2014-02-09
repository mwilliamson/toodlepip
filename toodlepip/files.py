import os

import spur
import mayo


_local = spur.LocalShell()

def copy(source, destination):
    if os.path.isdir(destination) and _is_git_repo(source):
        ignored_files = _find_ignored_files(source)
        
        for filename in all_filenames(source):
            if filename not in ignored_files and not filename.startswith(".git/"):
                copy(
                    os.path.join(source, filename),
                    os.path.join(destination, filename)
                )
    else:
        _local.run(["mkdir", "-p", os.path.dirname(destination)])
        _local.run(["cp", "-rT", source, destination])


def _find_ignored_files(path):
    result = _local.run(["git", "status", "-z", "--ignored"], cwd=path)
    lines = result.output.split(b"\0")
    ignore_prefix = b"!! "
    return [
        line[len(ignore_prefix):]
        for line in lines
        if line.startswith(ignore_prefix)
    ]

def _is_git_repo(path):
    repository = mayo.repository_at(path)
    if repository is None:
        return False
    if repository.type == "git":
        return True


def all_filenames(path):
    result = []
    for root, dirs, filenames in os.walk(path):
        for filename in filenames:
            full_path = os.path.join(root, filename)
            result.append(os.path.relpath(full_path, path))
    return result
