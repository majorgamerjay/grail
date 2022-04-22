# Made by MajorGamerJay <majorgamerjay@protonmail.com>

# Importing important modules
import argparse
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
        self.headers = []  # HTML/MD header files
        self.footers = []  # HTML/MD footer files
        self.others = []  # Other files, .css, .jpg, .png etc.

    # Adds MD files in self.files[]
    def add_md_files(self, path):
        for x in get_md_files(path):
            if x.startswith("_header"):
                self.headers.append(x)
            elif x.startswith("_footer"):
                self.footers.append(x)
            else:
                self.files.append(x)

    def add_other_files(self, path):
        for x in get_other_files(path):
            self.others.append(x)


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
        os.path.join(path, f)) and f.endswith(".md")]


# Adds markdown files in self.files[], self.headers[] and self.footers[]
# of MDDir object
for x in working_dirs:
    x.add_md_files(x.root)



# Return non-markdown files in designated directory
def get_other_files(path):
    return [f for f in os.listdir(path) if os.path.isfile(
        os.path.join(path, f)) and not f.endswith(".md")]


for x in working_dirs:
    x.add_other_files(x.root)

def debug_working_dirs():
    for x in working_dirs:
        print(f"""
        Root: {x.root}
        MD: {x.files}
        Headers: {x.headers}
        Footers: {x.footers}
        Others: {x.others}
        ---------------------""")

# Returns MD->HTML converted output
def lowdown(file):
    return subprocess.run(
            ['lowdown', file],
            stdout=subprocess.PIPE
        ).stdout.decode('utf-8')
