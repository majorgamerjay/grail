# Grail

### majorgamerjay
#### majorgamerjay@protonmail.com

Grail is a static website generator similar to
[ssg6](https://www.romanzolotarev.com/ssg.html) but made in python. It takes a 
source directory and a destination directory and copies the directory 
structure tree from the source directory to the destination directory, converts
the markdown files and copies the non-markdown files to the destination directory.

It supports adding headers and footers written in markdown and html.

## Usage

### Get Required Dependencies

1. python3
2. lowdown

### Directory structure:

Here is an example directory tree we will use to show usage of the program.

```
Website/
├─ src/
│  ├─ index.md
│  ├─ special.html
│  ├─ _header.html
│  ├─ _footer.html
│  ├─ style.css
│  ├─ script.js
│  ├─ subdir/
│  │  ├─ _header-01.md
│  │  ├─ _header-02.md
│  │  ├─ _header.html
│  │  ├─ file1.md
│  │  ├─ file2.md
│  │  ├─ _footer.html
│  │  ├─ _footer-02.md
│  │  ├─ _footer-01.md
│  ├─ subdir_two/
│  │  ├─ style_two.css
│  │  ├─ new_html.md
├─ docs/
│  ├─ .grail_target
├─ bin/
│  ├─ grail.py
```

`src` contains the source files needed for conversion and `docs` is the directory
in which the converted files will be located. The target directory should be marked
with a `.grail_target` file because the program deletes everything inside the directory
(like a reset) and then proceeds on with the conversion jobs.

After running,

`python3 bin/grail.py src dest` from the top directory in the website, the new
directory structure should be:


```
Website/
├─ src/
│  ├─ index.md
│  ├─ special.html
│  ├─ _header.html
│  ├─ _footer.html
│  ├─ style.css
│  ├─ script.js
│  ├─ subdir/
│  │  ├─ _header-01.md
│  │  ├─ _header-02.md
│  │  ├─ _header.html
│  │  ├─ file1.md
│  │  ├─ file2.md
│  │  ├─ _footer.html
│  │  ├─ _footer-02.md
│  │  ├─ _footer-01.md
│  ├─ subdir_two/
│  │  ├─ style_two.css
│  │  ├─ new_html.md
├─ docs/
│  ├─ .grail_target
│  ├─ index.html
│  ├─ special.html
│  ├─ _header.html
│  ├─ _footer.html
│  ├─ style.css
│  ├─ script.js
│  ├─ subdir/
│  │  ├─ _header.html
│  │  ├─ file1.html
│  │  ├─ file2.html
│  │  ├─ _footer.html
│  ├─ subdir_two/
│  │  ├─ style_two.css
│  │  ├─ new_html.html
├─ bin/
│  ├─ grail.py
```

Here, all the markdown files are converted into HTML. Unlike ssg6, this does not
have any incremental updates system and everything in /docs gets reset (in other words,
deleted or removed).

Contents from the `_header.html` and `_footer.html` files in a directory are prepended and 
appended to the markdown files in the directory. The header and footer files from
top-level directories does not interfere with the markdown files in subdirectories. Making
each directory its own isolated page.

There can only be one `_header.html` and `_footer.html` files in a directory but there can
be any number of markdown files that starts with `_header` and `_footer` and it will do its
job like the HTML header and footer files. This allows the static sites to have different
headers and footers in each subdirectory resulting in acquiring the ability to insert different
stylesheets and scripts.

Other files (non-md) are simply copied to their corresponding directory and no changes are made 
to them.

### Usage syntax:

`grail.py src dest`

Use python3 to run the program or use shebang to run it as a script directly.

## Acknowledgements

Inspired by [ssg6](https://www.romanzolotarev.com/ssg.html). Thanks to Roman Zolotarev for making 
such an awesome piece of software!

## License

MIT!
