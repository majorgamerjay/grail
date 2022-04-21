# Made by MajorGamerJay <majorgamerjay@protonmail.com>

# Importing important modules
import argparse
import glob
import os
import subprocess
import sys


# Defining MDDir object class
class MDDir:
    def __init__(
            self,
            root,
            ):
        self.root = root
        self.files = []
        self.headers = []
        self.footers = []

    # Adds MD files in self.files[]
    def add_md_files(self, path):
        for x in get_md_files(path):
            self.files.append(x)


# Declaring argument parser
parser = argparse.ArgumentParser(prog=f"{sys.argv[0]}", description="Static \
        website generator using lowdown and python based content management \
        system")
parser.add_argument("src", help="Source files directory")
parser.add_argument("dest", help="Destination documents directory")
args = parser.parse_args()

working_dirs = []  # list of MDDir objects to work in

# Append MDDir objects to working_dirs
for r, d, f in os.walk(os.getcwd()+'/'+args.src):
    working_dirs.append(MDDir(r))  # initialize with working dirs of source


# Returns markdown files in designated directory
def get_md_files(path):
    return [f for f in os.listdir(path) if os.path.isfile(
        os.path.join(path, f))]


# Adds markdown files in self.files[] of MDDir object
for x in working_dirs:
    x.add_md_files(x.root)


def lowdown(file):
    result = subprocess.run(
            ['lowdown', file],
            stdout=subprocess.PIPE
        ).stdout.decode('utf-8')
    return result
