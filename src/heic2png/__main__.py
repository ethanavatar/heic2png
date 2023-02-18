#!/usr/bin/env python3
from .heic2png import convert_from_dir, convert_from_file

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="heic2png", description="Convert HEIC files to PNG")
    subparsers = parser.add_subparsers(dest="command")

    parser_convert = subparsers.add_parser("dir", help="Convert all HEIC to PNG in a target directory")
    parser_convert.add_argument("dir", help="Target directory")
    parser_convert.add_argument("--delete", action="store_true", help="Delete the original HEIC files")
    parser_convert.add_argument("dest", help="Destination directory", default=None, nargs="?")

    parser_convert = subparsers.add_parser("file", help="Convert a single HEIC to PNG")
    parser_convert.add_argument("file", help="Target file")
    parser_convert.add_argument("--delete", action="store_true", help="Delete the original HEIC file")
    parser_convert.add_argument("dest", help="Destination directory", default=None, nargs="?")

    args = parser.parse_args()

    if args.command == "dir":
        convert_from_dir(args.dir, args.delete, args.dest)
    elif args.command == "file":
        convert_from_file(args.file, args.delete, args.dest)
    else:
        parser.print_help()