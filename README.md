# heic2png

A CLI tool to convert batches of images from HEIC to PNG.

## Installation

This tool is not published on PyPi yet, so you will have to install it from source until then.
```bash
$ pip install git+https://github.com/ethanavatar/heic2png.git
```

## Usage

```bash
$ python -m heic2png --help
usage: __main__.py [-h] {dir,file} ...

Convert HEIC to PNG

positional arguments:
  {dir,file}
    dir       Convert all HEIC to PNG in a target directory
    file      Convert a single HEIC to PNG

optional arguments:
  -h, --help  show this help message and exit
```

### Convert a single file

The following will result in a new file named `example.png` in the same directory as `example.heic`.
```bash
$ python -m heic2png example.heic
```

### Convert a directory

The following will result in a new `.png` file for each `.heic` file in the `path/to/heic/files` directory.
```bash
$ python -m heic2png dir path/to/heic/files
```

If you don't want to keep the original `.heic` files, you can use the `--delete` flag.
```bash
$ python -m heic2png dir path/to/heic/files --delete
```