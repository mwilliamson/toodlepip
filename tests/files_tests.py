import os
import tempfile
import shutil
import errno

import spur
from nose.tools import istest, assert_equal

from toodlepip import files


local = spur.LocalShell()


@istest
class FilesCopyTest(object):
    def setup(self):
        self._temp_dir = tempfile.mkdtemp()
        self._source_dir = os.path.join(self._temp_dir, "source")
        self._destination_dir = os.path.join(self._temp_dir, "destination")
        
    def teardown(self):
        shutil.rmtree(self._temp_dir)
    
    @istest
    def files_are_copied_when_not_part_of_a_source_control_repository(self):
        self._create_files(["a"])
        files.copy(self._source_dir, self._destination_dir)
        assert_equal(["a"], self._list_destination_files())
    
    
    @istest
    def files_in_subdirectories_are_copied(self):
        self._create_files(["a/b/c"])
        files.copy(self._source_dir, self._destination_dir)
        assert_equal(["a/b/c"], self._list_destination_files())
    
    
    @istest
    def destination_does_not_change_if_destination_directory_already_exists(self):
        self._create_files(["a/b/c"])
        os.mkdir(self._destination_dir)
        files.copy(self._source_dir, self._destination_dir)
        assert_equal(["a/b/c"], self._list_destination_files())
    
    
    @istest
    def files_ignored_by_git_are_ignored_by_copy(self):
        self._create_git_repo(
            filenames=["a", "b/a"],
            gitignore="/a"
        )
        os.mkdir(self._destination_dir)
        files.copy(self._source_dir, self._destination_dir)
        assert_equal([".gitignore", "b/a"], self._list_destination_files())

    def _create_files(self, filenames):
        os.mkdir(self._source_dir)
        for filename in filenames:
            path = os.path.join(self._source_dir, filename)
            _mkdir_p(os.path.dirname(path))
            with open(path, "w") as target:
                target.write("")
    
    def _create_git_repo(self, filenames, gitignore):
        self._create_files(filenames)
        with open(os.path.join(self._source_dir, ".gitignore"), "w") as gitignore_file:
            gitignore_file.write(gitignore)
        local.run(["git", "init"], cwd=self._source_dir)
    
    def _list_destination_files(self):
        return list(files.all_filenames(self._destination_dir))


def _mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise
