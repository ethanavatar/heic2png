from __future__ import annotations
import typing as t

import argparse
import os

from tqdm import tqdm

from PIL import Image
import pillow_heif

def convert_from_file(file: str, delete: bool = False, dest_dir: str = None) -> str:
    """Convert a single HEIC file to PNG"""
    file = os.path.abspath(file)
    heif_file = pillow_heif.read_heif(file)
    image = Image.frombytes(heif_file.mode, heif_file.size, heif_file.data, "raw", heif_file.mode, heif_file.stride)
    new_name = os.path.splitext(file)[0] + ".png"

    if dest_dir:
        new_name = os.path.join(dest_dir, os.path.basename(new_name))

    image.save(new_name)

    if delete:
        os.remove(file)

    return new_name

def convert_from_dir(dir: str, delete: bool = False, dest_dir: str = None):
    """Convert all HEIC files in a directory to PNG"""
    dir = os.path.abspath(dir)

    targets = [
        f for f in os.listdir(dir)
        if f.lower().endswith(".heic") or f.lower().endswith(".heif")
    ]

    progress_bar = tqdm(total=len(targets), desc="Converting...", )

    completed: list[str] = []

    try:
        for file in targets:
            new_file = convert_from_file(os.path.join(dir, file), delete, dest_dir)
            completed.append(new_file)
            progress_bar.update(1)

    except KeyboardInterrupt:
        print("Interrupted by user")
        if delete:
            print("Removing processed files...")
            for file in completed:
                os.remove(file)