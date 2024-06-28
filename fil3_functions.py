import base64
import hashlib
import os
import random
import string


def corrupt_file(file_path, corruption_percentage=10):
    # Read the original file data
    with open(file_path, 'rb') as file:
        data = bytearray(file.read())

    total_bytes = len(data)
    bytes_to_corrupt = int(total_bytes * corruption_percentage / 100)

    # Randomly select byte positions to corrupt
    for _ in range(bytes_to_corrupt):
        byte_position = random.randint(0, total_bytes - 1)
        data[byte_position] = random.randint(0, 255)

    # Write the corrupted data back to the file
    corrupted_file_path = file_path + '.corrupted'
    with open(corrupted_file_path, 'wb') as corrupted_file:
        corrupted_file.write(data)

    return corrupted_file_path


# Example usage
file_path = 'path/to/your/file.ext'
corrupt_file(file_path, 10)


def generate_random_bytes_file():
    # Function to convert size to bytes
    def size_to_bytes(size, size_unit):
        size_unit = size_unit.lower()
        if size_unit == "b":
            return size  # bytes
        elif size_unit == "kb":
            return size * (1000 ** 1)  # Kilobytes
        elif size_unit == "mb":
            return size * (1000 ** 2)  # Megabytes
        elif size_unit == "gb":
            return size * (1000 ** 3)  # Gigabytes
        elif size_unit == "kib":
            return size * (1024 ** 1)  # Kibibytes
        elif size_unit == "mib":
            return size * (1024 ** 2)  # Mebibytes
        elif size_unit == "gib":
            return size * (1024 ** 3)  # Gibibytes
        else:
            raise ValueError("Invalid unit. Choose from 'B', 'KB', 'MB', 'GB', 'KiB', 'MiB', 'GiB'.")

    # User input for file size
    n = int(input("Enter the size of the file: "))
    unit = input("Enter the unit (B, KB, MB, GB // KiB, MiB, GiB ): ")

    # Convert size to bytes
    size_in_bytes = size_to_bytes(n, unit)

    # Generate random bytes
    random_bytes = os.urandom(size_in_bytes)

    # User input for file name
    file_name = input("Enter the file name: ")

    # List of file extensions
    predefined_extensions = ['.txt', '.bin', '.dat']

    # User input for file extension
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

    # Append the extension bytes to the file
    file_path = file_name + file_extension

    # Save the random bytes to the file
    with open(file_path, 'wb') as file:
        file.write(random_bytes)

    print(f"File '{file_path}' created with {size_in_bytes} bytes of random data.")


def generate_multiple_random_files():
    # Function to convert size to bytes
    def size_to_bytes(size, size_unit):
        size_unit = size_unit.lower()
        if size_unit == "b":
            return size  # bytes
        elif size_unit == "kb":
            return size * (1000 ** 1)  # Kilobytes
        elif size_unit == "mb":
            return size * (1000 ** 2)  # Megabytes
        elif size_unit == "gb":
            return size * (1000 ** 3)  # Gigabytes
        elif size_unit == "kib":
            return size * (1024 ** 1)  # Kibibytes
        elif size_unit == "mib":
            return size * (1024 ** 2)  # Mebibytes
        elif size_unit == "gib":
            return size * (1024 ** 3)  # Gibibytes
        else:
            raise ValueError("Invalid unit. Choose from 'B', 'KB', 'MB', 'GB', 'KiB', 'MiB', 'GiB'.")

    # Function to generate random filename
    def generate_random_filename(length, extension):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length)) + extension

    # Function to generate numbered filename
    def generate_numbered_filename(base, i, digits, extension):
        return f"{base}{str(i).zfill(digits)}{extension}"

    # User input for number of files
    num_files = int(input("Enter the number of files to create: "))

    # User input for file size
    file_size_n = int(input("Enter the size of each file: "))
    file_size_unit = input("Enter the unit (Bytes, KB, MB, GB): ")

    # Convert size to bytes
    size_in_bytes = size_to_bytes(file_size_n, file_size_unit)

    # User input for filename pattern
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


# splitting files to n pieces
def split_file(file_path, num_pieces):
    with open(file_path, 'rb') as file:
        data = file.read()

    part_size = len(data) // num_pieces
    parts = [data[i * part_size: (i + 1) * part_size] for i in range(num_pieces)]

    # Ensure the parts are not useful on their own
    hash_l = hashlib.sha256(data).digest()
    parts = [part + hash_l for part in parts]

    for i, part in enumerate(parts):
        with open(f'{file_path}.part{i}', 'wb') as part_file:
            part_file.write(part)


# Rejoining the split files
def join_files(file_path, num_pieces):
    parts = []
    for i in range(num_pieces):
        with open(f'{file_path}.part{i}', 'rb') as part_file:
            parts.append(part_file.read())

    hash_l = parts[0][-32:]
    data = b''.join([part[:-32] for part in parts])

    # Verify hash to ensure integrity
    if hashlib.sha256(data).digest() != hash_l:
        raise ValueError("Files do not match original hash")

    with open(file_path, 'wb') as file:
        file.write(data)


def base64_encode(file_path):
    with open(file_path, 'rb') as file:
        encoded_data = base64.b64encode(file.read())

    with open(f'{file_path}.b64', 'wb') as encoded_file:
        encoded_file.write(encoded_data)


def base64_decode(file_path):
    with open(file_path, 'rb') as file:
        decoded_data = base64.b64decode(file.read())

    original_file_path = file_path.replace('.b64', '')
    with open(original_file_path, 'wb') as decoded_file:
        decoded_file.write(decoded_data)


def sha256_checksum(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for block in iter(lambda: f.read(4096), b''):
            sha256.update(block)
    return sha256.hexdigest()


def compare_files(file_path1, file_path2):
    checksum1 = sha256_checksum(file_path1)
    checksum2 = sha256_checksum(file_path2)
    return checksum1 == checksum2


"""
EoF signatures will be added to files that have them for corrupt file gen and multiple file gens.
Steganography for both files, executables and regular text planned to be added.

"""
eof_signatures = {
    "ai": None,  # Adobe Illustrator - no fixed EOF signature
    "psd": None,  # Adobe Photoshop - no fixed EOF signature
    "dwg": None,  # AutoCAD - no fixed EOF signature
    "mp3": None,  # Audio - no fixed EOF signature
    "wav": None,  # Audio - no fixed EOF signature
    "wma": None,  # Audio - no fixed EOF signature
    "bak": None,  # Backup - no fixed EOF signature
    "torrent": None,  # BitTorrent - no fixed EOF signature
    "7z": None,  # Compressed - no fixed EOF signature
    "tar.gz": None,  # Compressed - no fixed EOF signature
    "rar": None,  # Compressed - no fixed EOF signature
    "zip": None,  # Compressed - no fixed EOF signature
    "iso": None,  # Disc image - no fixed EOF signature
    "pdf": b'%EOF',  # Document
    "exe": None,  # Executable - no fixed EOF signature
    "otf": None,  # Font - no fixed EOF signature
    "ttf": None,  # Font - no fixed EOF signature
    "ico": None,  # Icon - no fixed EOF signature
    "bmp": None,  # Image - no fixed EOF signature
    "gif": b'\x00\x3B',  # Image
    "jpeg": b'\xFF\xD9',  # Image
    "jpg": b'\xFF\xD9',  # Image
    "png": b'\x49\x45\x4E\x44\xAE\x42\x60\x82',  # Image
    "svg": None,  # Image - no fixed EOF signature
    "msi": None,  # Installer - no fixed EOF signature
    "csv": None,  # Microsoft Excel - no fixed EOF signature
    "xls": None,  # Microsoft Excel - no fixed EOF signature
    "xlsx": None,  # Microsoft Excel - no fixed EOF signature
    "pps": None,  # Microsoft PowerPoint - no fixed EOF signature
    "ppt": None,  # Microsoft PowerPoint - no fixed EOF signature
    "pptx": None,  # Microsoft PowerPoint - no fixed EOF signature
    "doc": None,  # Microsoft Word - no fixed EOF signature
    "docx": None,  # Microsoft Word - no fixed EOF signature
    "mid": None,  # MIDI - no fixed EOF signature
    "txt": None,  # Plain text - no fixed EOF signature
    "tmp": None,  # Temporary - no fixed EOF signature
    "vcr": None,  # VCard - no fixed EOF signature
    "avi": None,  # Video - no fixed EOF signature
    "mp4": None,  # Video - no fixed EOF signature
    "mpg": None,  # Video - no fixed EOF signature
    "wmv": None,  # Video - no fixed EOF signature
    "xhtml": None,  # Web page - no fixed EOF signature
    "html": None,  # Web page - no fixed EOF signature
}
