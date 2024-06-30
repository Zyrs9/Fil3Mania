import base64
import hashlib
import os
import random
import shutil
import string
import numpy as np
from PIL import Image
from typing import List, Optional


def corrupt_file(file_path: str, corruption_percentage: int = 10) -> str:
    with open(file_path, 'rb') as file:
        data = bytearray(file.read())

    total_bytes = len(data)
    bytes_to_corrupt = int(total_bytes * corruption_percentage / 100)

    for _ in range(bytes_to_corrupt):
        byte_position = random.randint(0, total_bytes - 1)
        data[byte_position] = random.randint(0, 255)

    corrupted_file_path = file_path + '.corrupted'
    with open(corrupted_file_path, 'wb') as corrupted_file:
        corrupted_file.write(data)

    return corrupted_file_path


def generate_random_bytes_file() -> None:
    def size_to_bytes(size: int, size_unit: str) -> int:
        size_unit = size_unit.lower()
        if size_unit == "b":
            return size
        elif size_unit == "kb":
            return size * (1000 ** 1)
        elif size_unit == "mb":
            return size * (1000 ** 2)
        elif size_unit == "gb":
            return size * (1000 ** 3)
        elif size_unit == "kib":
            return size * (1024 ** 1)
        elif size_unit == "mib":
            return size * (1024 ** 2)
        elif size_unit == "gib":
            return size * (1024 ** 3)
        else:
            raise ValueError("Invalid unit. Choose from 'B', 'KB', 'MB', 'GB', 'KiB', 'MiB', 'GiB'.")

    n = int(input("Enter the size of the file: "))
    unit = input("Enter the unit (B, KB, MB, GB // KiB, MiB, GiB ): ")
    size_in_bytes = size_to_bytes(n, unit)
    random_bytes = os.urandom(size_in_bytes)
    file_name = input("Enter the file name: ")
    predefined_extensions = ['.txt', '.bin', '.dat']

    print("Choose a file extension from the list or enter a custom extension:")
    for i, ext in enumerate(predefined_extensions):
        print(f"{i + 1}. {ext}")
    print(f"{len(predefined_extensions) + 1}. Custom extension")
    print(f"{len(predefined_extensions) + 2}. No extension")

    choice = int(input("Enter your choice: "))
    if 1 <= choice <= len(predefined_extensions):
        file_extension = predefined_extensions[choice - 1]
    elif choice == len(predefined_extensions) + 1:
        file_extension = input("Enter your custom extension (including dot): ")
    elif choice == len(predefined_extensions) + 2:
        file_extension = ''
    else:
        raise ValueError("Invalid choice.")

    file_path = file_name + file_extension
    with open(file_path, 'wb') as file:
        file.write(random_bytes)

    print(f"File '{file_path}' created with {size_in_bytes} bytes of random data.")


def generate_multiple_random_files() -> None:
    def size_to_bytes(size: int, size_unit: str) -> int:
        size_unit = size_unit.lower()
        if size_unit == "b":
            return size
        elif size_unit == "kb":
            return size * (1000 ** 1)
        elif size_unit == "mb":
            return size * (1000 ** 2)
        elif size_unit == "gb":
            return size * (1000 ** 3)
        elif size_unit == "kib":
            return size * (1024 ** 1)
        elif size_unit == "mib":
            return size * (1024 ** 2)
        elif size_unit == "gib":
            return size * (1024 ** 3)
        else:
            raise ValueError("Invalid unit. Choose from 'B', 'KB', 'MB', 'GB', 'KiB', 'MiB', 'GiB'.")

    def generate_random_filename(length: int, extension: str) -> str:
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length)) + extension

    def generate_numbered_filename(base: str, characters: int, digits_fill: int, extension: str) -> str:
        return f"{base}{str(characters).zfill(digits_fill)}{extension}"

    num_files = int(input("Enter the number of files to create: "))
    file_size_n = int(input("Enter the size of each file: "))
    file_size_unit = input("Enter the unit (Bytes, KB, MB, GB): ")
    size_in_bytes = size_to_bytes(file_size_n, file_size_unit)

    print("Choose the filename pattern:")
    print("1. Random (you can specify the number of characters in the filename)")
    print("2. Numbered (choose from 0, 1, ..., 00, 01, ..., 1, 2, ..., 01, 02, ...)")
    print("3. Custom with numbers (e.g., 'file_%_name' where '%' will be replaced with numbers)")

    pattern_choice = int(input("Enter your choice: "))

    if pattern_choice == 1:
        filename_length = int(input("Enter the number of characters for the filename: "))
        print("Choose a file extension from the list or enter a custom extension:")
        predefined_extensions = ['.txt', '.bin', '.dat']
        for i, ext in enumerate(predefined_extensions):
            print(f"{i + 1}. {ext}")
        print(f"{len(predefined_extensions) + 1}. Custom extension")

        ext_choice = int(input("Enter your choice: "))
        if 1 <= ext_choice <= len(predefined_extensions):
            file_extension = predefined_extensions[ext_choice - 1]
        else:
            file_extension = input("Enter your custom extension (including dot): ")

        for _ in range(num_files):
            filename = generate_random_filename(filename_length, file_extension)
            with open(filename, 'wb') as file:
                file.write(os.urandom(size_in_bytes))
            print(f"File '{filename}' created with {size_in_bytes} bytes of random data.")
    elif pattern_choice == 2:
        numbering_options = ["0, 1, ...", "00, 01, ...", "1, 2, ...", "01, 02, ..."]
        for i, option in enumerate(numbering_options):
            print(f"{i + 1}. {option}")

        numbering_choice = int(input("Enter your numbering choice: "))
        if numbering_choice == 1:
            digits = 1
            start = 0
        elif numbering_choice == 2:
            digits = 2
            start = 0
        elif numbering_choice == 3:
            digits = 1
            start = 1
        elif numbering_choice == 4:
            digits = 2
            start = 1
        else:
            raise ValueError("Invalid numbering choice.")

        print("Choose a file extension from the list or enter a custom extension:")
        predefined_extensions = ['.txt', '.bin', '.dat']
        for i, ext in enumerate(predefined_extensions):
            print(f"{i + 1}. {ext}")
        print(f"{len(predefined_extensions) + 1}. Custom extension")

        ext_choice = int(input("Enter your choice: "))
        if 1 <= ext_choice <= len(predefined_extensions):
            file_extension = predefined_extensions[ext_choice - 1]
        else:
            file_extension = input("Enter your custom extension (including dot): ")

        for i in range(start, start + num_files):
            filename = generate_numbered_filename("", i, digits, file_extension)
            with open(filename, 'wb') as file:
                file.write(os.urandom(size_in_bytes))
            print(f"File '{filename}' created with {size_in_bytes} bytes of random data.")
    elif pattern_choice == 3:
        custom_pattern = input("Enter the custom filename pattern (use '%' for numbering): ")
        numbering_options = ["0, 1, ...", "00, 01, ...", "1, 2, ...", "01, 02, ..."]
        for i, option in enumerate(numbering_options):
            print(f"{i + 1}. {option}")

        numbering_choice = int(input("Enter your numbering choice: "))
        if numbering_choice == 1:
            digits = 1
            start = 0
        elif numbering_choice == 2:
            digits = 2
            start = 0
        elif numbering_choice == 3:
            digits = 1
            start = 1
        elif numbering_choice == 4:
            digits = 2
            start = 1
        else:
            raise ValueError("Invalid numbering choice.")

        print("Choose a file extension from the list or enter a custom extension:")
        predefined_extensions = ['.txt', '.bin', '.dat']
        for i, ext in enumerate(predefined_extensions):
            print(f"{i + 1}. {ext}")
        print(f"{len(predefined_extensions) + 1}. Custom extension")

        ext_choice = int(input("Enter your choice: "))
        if 1 <= ext_choice <= len(predefined_extensions):
            file_extension = predefined_extensions[ext_choice - 1]
        else:
            file_extension = input("Enter your custom extension (including dot): ")

        for i in range(start, start + num_files):
            filename = custom_pattern.replace("%", str(i).zfill(digits)) + file_extension
            with open(filename, 'wb') as file:
                file.write(os.urandom(size_in_bytes))
            print(f"File '{filename}' created with {size_in_bytes} bytes of random data.")
    else:
        print("Invalid choice.")


def split_file(file_path: str, num_pieces: int) -> None:
    with open(file_path, 'rb') as file:
        data = file.read()

    part_size = len(data) // num_pieces
    parts = [data[i * part_size: (i + 1) * part_size] for i in range(num_pieces)]

    hash_l = hashlib.sha256(data).digest()
    parts = [part + hash_l for part in parts]

    for i, part in enumerate(parts):
        with open(f'{file_path}.part{i}', 'wb') as part_file:
            part_file.write(part)


def join_files(file_path: str, num_pieces: int) -> None:
    parts: List[bytes] = []
    for i in range(num_pieces):
        with open(f'{file_path}.part{i}', 'rb') as part_file:
            parts.append(part_file.read())

    hash_l = parts[0][-32:]
    data = b''.join([part[:-32] for part in parts])

    if hashlib.sha256(data).digest() != hash_l:
        raise ValueError("Files do not match original hash")

    with open(file_path, 'wb') as file:
        file.write(data)


def base64_encode(file_path: str) -> None:
    with open(file_path, 'rb') as file:
        encoded_data = base64.b64encode(file.read())

    with open(f'{file_path}.b64', 'wb') as encoded_file:
        encoded_file.write(encoded_data)


def base64_decode(file_path: str) -> None:
    with open(file_path, 'rb') as file:
        decoded_data = base64.b64decode(file.read())

    original_file_path = file_path.replace('.b64', '')
    with open(original_file_path, 'wb') as decoded_file:
        decoded_file.write(decoded_data)


def sha256_checksum(file_path: str) -> str:
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for block in iter(lambda: f.read(4096), b''):
            sha256.update(block)
    return sha256.hexdigest()


def compare_files(file_path1: str, file_path2: str) -> bool:
    checksum1 = sha256_checksum(file_path1)
    checksum2 = sha256_checksum(file_path2)
    return checksum1 == checksum2


def hide_text_in_image(image_path: str, text: str, output_path: str) -> str:
    image = Image.open(image_path)
    image_data = np.array(image)

    binary_text = ''.join(format(ord(char), '08b') for char in text)
    binary_text += '1111111111111110'

    data_index = 0
    for row in range(image_data.shape[0]):
        for col in range(image_data.shape[1]):
            for color in range(image_data.shape[2]):
                if data_index < len(binary_text):
                    image_data[row, col, color] = (image_data[row, col, color] & 0xFE) | int(binary_text[data_index])
                    data_index += 1

    result_image = Image.fromarray(image_data)
    result_image.save(output_path)
    return output_path


def reveal_text_in_image(image_path: str) -> str:
    image = Image.open(image_path)
    image_data = np.array(image)

    binary_text = ""
    for row in range(image_data.shape[0]):
        for col in range(image_data.shape[1]):
            for color in range(image_data.shape[2]):
                binary_text += str(image_data[row, col, color] & 1)

    chars = [chr(int(binary_text[i:i + 8], 2)) for i in range(0, len(binary_text), 8)]
    text = ''.join(chars)

    end_marker_index = text.find(chr(255) + chr(254))
    if end_marker_index != -1:
        text = text[:end_marker_index]

    return text


def hide_image_in_image(cover_image_path: str, secret_image_path: str, output_path: str) -> str:
    cover_image = Image.open(cover_image_path)
    secret_image = Image.open(secret_image_path).resize(cover_image.size)

    cover_image_data = np.array(cover_image)
    secret_image_data = np.array(secret_image)

    secret_image_binary = ''.join(format(pixel, '08b') for pixel in secret_image_data.flatten())

    data_index = 0
    for row in range(cover_image_data.shape[0]):
        for col in range(cover_image_data.shape[1]):
            for color in range(cover_image_data.shape[2]):
                if data_index < len(secret_image_binary):
                    cover_image_data[row, col, color] = (cover_image_data[row, col, color] & 0xFE) | int(
                        secret_image_binary[data_index])
                    data_index += 1

    result_image = Image.fromarray(cover_image_data)
    result_image.save(output_path)
    return output_path


def reveal_image_in_image(image_path: str, output_path: str) -> str:
    image = Image.open(image_path)
    image_data = np.array(image)

    binary_secret_image = ""
    for row in range(image_data.shape[0]):
        for col in range(image_data.shape[1]):
            for color in range(image_data.shape[2]):
                binary_secret_image += str(image_data[row, col, color] & 1)

    secret_image_data = [int(binary_secret_image[i:i + 8], 2) for i in range(0, len(binary_secret_image), 8)]
    secret_image_data = np.array(secret_image_data).reshape(image_data.shape).astype(np.uint8)

    secret_image = Image.fromarray(secret_image_data)
    secret_image.save(output_path)
    return output_path


def hide_data_in_image(image_path: str, data: bytes, output_path: str) -> str:
    image = Image.open(image_path)
    image_data = np.array(image)

    binary_data = ''.join(format(byte, '08b') for byte in data)
    binary_data += '1111111111111110'

    data_index = 0
    for row in range(image_data.shape[0]):
        for col in range(image_data.shape[1]):
            for color in range(image_data.shape[2]):
                if data_index < len(binary_data):
                    image_data[row, col, color] = (image_data[row, col, color] & 0xFE) | int(binary_data[data_index])
                    data_index += 1

    result_image = Image.fromarray(image_data)
    result_image.save(output_path)
    return output_path


def reveal_data_in_image(image_path: str) -> bytes:
    image = Image.open(image_path)
    image_data = np.array(image)

    binary_data = ""
    for row in range(image_data.shape[0]):
        for col in range(image_data.shape[1]):
            for color in range(image_data.shape[2]):
                binary_data += str(image_data[row, col, color] & 1)

    data = bytes([int(binary_data[i:i + 8], 2) for i in range(0, len(binary_data), 8)])

    end_marker_index = data.find(b'\xff\xfe')
    if end_marker_index != -1:
        data = data[:end_marker_index]

    return data


eof_signatures: dict[str, Optional[bytes]] = {
    "ai": None,
    "psd": None,
    "dwg": None,
    "mp3": None,
    "wav": None,
    "wma": None,
    "bak": None,
    "torrent": None,
    "7z": None,
    "tar.gz": None,
    "rar": None,
    "zip": None,
    "iso": None,
    "pdf": b'%EOF',
    "exe": None,
    "otf": None,
    "ttf": None,
    "ico": None,
    "bmp": None,
    "gif": b'\x00\x3B',
    "jpeg": b'\xFF\xD9',
    "jpg": b'\xFF\xD9',
    "png": b'\x49\x45\x4E\x44\xAE\x42\x60\x82',
    "svg": None,
    "msi": None,
    "csv": None,
    "xls": None,
    "xlsx": None,
    "pps": None,
    "ppt": None,
    "pptx": None,
    "doc": None,
    "docx": None,
    "mid": None,
    "txt": None,
    "tmp": None,
    "vcr": None,
    "avi": None,
    "mp4": None,
    "mpg": None,
    "wmv": None,
    "xhtml": None,
    "html": None,
}


def create_folder_for_sort1(path: str, extension: str) -> str:
    folder_name: str = extension[1:]
    folder_path: str = os.path.join(path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path


def sort_files_for_sort1(source_path: str) -> None:
    for root_dir, sub_dir, filenames in os.walk(source_path):
        for filename in filenames:
            file_path: str = os.path.join(root_dir, filename)
            extension: str = os.path.splitext(filename)[1]

            if extension:
                target_folder: str = create_folder_for_sort1(source_path, extension)
                target_path: str = os.path.join(target_folder, filename)

                shutil.move(file_path, target_path)


def remove_empty_folders_for_sort1(source_path: str) -> None:
    for root_dir, sub_dir, filenames in os.walk(source_path, topdown=False):
        for current_dir in sub_dir:
            folder_path: str = os.path.join(root_dir, current_dir)
            if not os.listdir(folder_path):
                os.rmdir(folder_path)


def file_sort1(usr_input: str) -> None:
    if os.path.exists(path=usr_input):
        sort_files_for_sort1(usr_input)
        remove_empty_folders_for_sort1(usr_input)
        print("Files sorted successfully")
    else:
        print("Invalid path")
