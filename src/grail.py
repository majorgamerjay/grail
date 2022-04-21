# Made by MajorGamerJay <majorgamerjay@protonmail.com>

# Importing important modules
import argparse
import subprocess
import sys


# Defining MDDir object class
class MDDir:
    def __init__(
            self,
            root,
            ):
        self.root = root

    headers = []
    footers = []


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
    return result
