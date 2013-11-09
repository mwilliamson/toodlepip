import argparse
import sys

import spur

from .build import Builder



def run(argv):
    args = _parse_args(argv)
    exit(args.func(args))


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
        builder = Builder(spur.LocalShell(), sys.stdout)
        builder.build(args.path)
