# Made by MajorGamerJay <majorgamerjay@protonmail.com>

# Importing important modules
import sys
import argparse
import subprocess


# Defining MDFile object class
class MDFile:
    def __init__(
            self,
            path,
            header,
            footer
            ):
        self.path = path
        self.header = header
        self.footer = footer

# Declaring argument parser
parser = argparse.ArgumentParser(prog=f"{sys.argv[0]}", description="Static \
        website generator using lowdown and python based content management \
        system")
parser.add_argument("src", help="Source files directory")
parser.add_argument("dest", help="Destination documents directory")
args = parser.parse_args()


def lowdown(file):
    result = subprocess.run(
            ['lowdown', file],
            stdout=subprocess.PIPE
        ).stdout.decode('utf-8')
