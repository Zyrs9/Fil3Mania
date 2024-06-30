# File Manipulation and Steganography Toolkit

## Description
This project provides a set of tools for manipulating files and performing steganography. It includes functions for corrupting files, generating random byte files, splitting and joining files, encoding and decoding files in base64, calculating file checksums, comparing files, hiding text or images in images, and more.

## Features
- Corrupt files by a given percentage.
- Generate files with random bytes.
- Split files into multiple pieces and join them back.
- Encode and decode files in base64.
- Calculate the SHA-256 checksum of files.
- Compare two files by their checksums.
- Hide text or other data within images.
- Hide one image within another.

## Requirements
- Python > 3.10.x
- `numpy`
- `Pillow`

## Installation
To install the required packages, run:
```bash
pip install numpy pillow
```
## Usage

This toolkit is menu-driven. Run the script and follow the prompts to use the various functions.

## Running the Script

```bash 
python fil3Mania.py
```


## Menu Options
````
0   Exit: Exits the menu.
1   corrupt_file: Corrupts a file by a specified percentage.
2   generate_random_bytes_file: Generates a file with random bytes.
3   generate_multiple_random_files: Generates multiple files with random bytes.
4   split_file: Splits a file into multiple pieces.
5   join_files: Joins multiple pieces of a file back together.
6   base64_encode: Encodes a file in base64.
7   base64_decode: Decodes a base64 encoded file.
8   sha256_checksum: Calculates the SHA-256 checksum of a file.
9   compare_files: Compares two files by their checksums.
10  hide_text_in_image: Hides text within an image.
11  reveal_text_in_image: Reveals hidden text within an image.
12  hide_image_in_image: Hides one image within another.
13  reveal_image_in_image: Reveals a hidden image within another image.
14  hide_data_in_image: Hides binary data within an image.
15  reveal_data_in_image: Reveals hidden binary data within an image.
16  file_sort1: Sorts the files and documents in the dir by their extensions into sub_dirs.
````
