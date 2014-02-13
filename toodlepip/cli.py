import argparse
import sys
import os

import spur

from .build import create_builder


def run(argv):
    args = _parse_args(argv)
    exit(args.func(args).return_code)


def _parse_args(argv):
    commands = [
        BuildCommand(),
    ]
    
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    
    for command in commands:
        subparser = subparsers.add_parser(command.name)
        subparser.set_defaults(func=command.execute)
        command.create_parser(subparser)

    return parser.parse_args(argv[1:])


class BuildCommand(object):
    name = "build"
    
    def create_parser(self, subparser):
        subparser.add_argument("path")
    
    def execute(self, args):
        with os.fdopen(sys.stdout.fileno(), "wb") as binary_stdout:
            builder = create_builder(spur.LocalShell(), binary_stdout)
            return builder.build(args.path)
