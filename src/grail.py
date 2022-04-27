# Made by MajorGamerJay <majorgamerjay@protonmail.com>

import argparse
import os
import subprocess
import sys
import shutil


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


def check_if_target_is_valid(dest):
    if os.path.isfile(os.path.join(dest, ".grail_target")):
        return True
    else:
        return False


# Returns markdown files in designated directory
def get_md_files(path):
    return [f for f in os.listdir(path) if os.path.isfile(
        os.path.join(path, f)) and f.endswith(".md")]


# Return non-markdown files in designated directory
def get_other_files(path):
    return [f for f in os.listdir(path) if os.path.isfile(
        os.path.join(path, f)) and not f.endswith(".md")]


def create_target_validation(dest):
    file = open(os.path.join(dest, ".grail_target"), 'x')
    file.close()


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
            [
                'lowdown',
                '--html-no-escapehtml',
                '--html-no-skiphtml',
                '--parse-no-metadata',
                '--parse-no-autolink',
                file
            ],
            stdout=subprocess.PIPE
        ).stdout.decode('utf-8')


# Convert individual files and append with lowdown
def convert_individual_file(headers, footers, path, root):
    body = lowdown(path)

    for header in headers:
        body = lowdown(os.path.join(root, header)) + body
    for footer in footers:
        body = body + lowdown(os.path.join(root, footer))

    # This part checks for _header.html, _footer.html and appends it
    if os.path.isfile(os.path.join(root, '_header.html')):
        with open(os.path.join(root, '_header.html'), "r") as header:
            body = header.read() + '\n' + body

    if os.path.isfile(os.path.join(root, '_footer.html')):
        with open(os.path.join(root, '_footer.html'), "r") as footer:
            body = body + '\n' + footer.read()

    return body


def shutil_ignore_callback(src, files):
    return [f for f in files if os.path.isfile(os.path.join(src, f))]


# Make destination directories
def make_dest_dirs(src, dest):
    if os.path.exists(dest):  # note: if directory exists, it gets deleted
        shutil.rmtree(dest)

    shutil.copytree(
            src,
            dest,
            ignore=shutil_ignore_callback)


# Main convert-append-copy job
def copy_job(src, dest):
    prefix_index = len(os.path.abspath(src)) + len(os.path.sep)

    for mddir in working_dirs:
        relative = mddir.root[prefix_index:]  # relative directory from source

        for file in mddir.files:
            with open(os.path.join(
                dest,
                relative,
                file[:-2]+"html"), 'x') as writable:
                writable.write(
                        convert_individual_file(
                            mddir.headers,
                            mddir.footers,
                            os.path.join(src, relative, file),
                            mddir.root))

        for other in mddir.others:
            shutil.copyfile(
                    os.path.join(src, relative, other),
                    os.path.join(dest, relative, other))


# Declaring argument parser
parser = argparse.ArgumentParser(prog=f"{sys.argv[0]}", description="Static \
        website generator using lowdown and python based content management \
        system")
parser.add_argument("src", help="Source files directory")
parser.add_argument("dest", help="Destination documents directory")
args = parser.parse_args()

working_dirs = []  # list of MDDir objects to work in

# Append MDDir objects to working_dirs
for r, d, f in os.walk(args.src):
    working_dirs.append(MDDir(os.path.abspath(r)))  # initialize with working dirs of source


# Adds markdown files in self.files[], self.headers[] and self.footers[]
# of MDDir object
for x in working_dirs:
    x.add_md_files(x.root)


# Adds other files in self.others[]
for x in working_dirs:
    x.add_other_files(x.root)


if check_if_target_is_valid(args.dest):
    make_dest_dirs(args.src, args.dest)
    copy_job(args.src, args.dest)
    create_target_validation(args.dest)
else:
    print("Given destination directory does not have .grail_target,\
            grail will not generate!.")
