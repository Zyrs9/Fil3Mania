from fil3_functions import (
    corrupt_file,
    generate_random_bytes_file,
    generate_multiple_random_files,
    split_file,
    join_files,
    base64_encode,
    base64_decode,
    sha256_checksum,
    compare_files,
    hide_text_in_image,
    reveal_text_in_image,
    hide_image_in_image,
    reveal_image_in_image,
    hide_data_in_image,
    reveal_data_in_image,
    file_sort1
)


def show_menu() -> None:
    print("Select a function to see its example usage:\n"
          "1. corrupt_file\n"
          "2. generate_random_bytes_file\n"
          "3. generate_multiple_random_files\n"
          "4. split_file\n"
          "5. join_files\n"
          "6. base64_encode\n"
          "7. base64_decode\n"
          "8. sha256_checksum\n"
          "9. compare_files\n"
          "10. hide_text_in_image\n"
          "11. reveal_text_in_image\n"
          "12. hide_image_in_image\n"
          "13. reveal_image_in_image\n"
          "14. hide_data_in_image\n"
          "15. reveal_data_in_image\n"
          "16. file_sort1\n"
          "0. Exit"
          )


def main() -> None:
    while True:
        show_menu()
        choice = int(input("Enter your choice: "))

        match choice:
            case 0:
                break
            case 1:
                file_path = input("Enter the file path: ")
                corruption_percentage = int(input("Enter the corruption percentage: "))
                print(f"Corrupted file path: {corrupt_file(file_path, corruption_percentage)}")
            case 2:
                generate_random_bytes_file()
            case 3:
                generate_multiple_random_files()
            case 4:
                file_path = input("Enter the file path: ")
                num_pieces = int(input("Enter the number of pieces: "))
                split_file(file_path, num_pieces)
            case 5:
                file_path = input("Enter the file path: ")
                num_pieces = int(input("Enter the number of pieces: "))
                join_files(file_path, num_pieces)
            case 6:
                file_path = input("Enter the file path: ")
                base64_encode(file_path)
            case 7:
                file_path = input("Enter the file path: ")
                base64_decode(file_path)
            case 8:
                file_path = input("Enter the file path: ")
                print(f"SHA-256 checksum: {sha256_checksum(file_path)}")
            case 9:
                file_path1 = input("Enter the first file path: ")
                file_path2 = input("Enter the second file path: ")
                print(f"Files are {'the same' if compare_files(file_path1, file_path2) else 'different'}")
            case 10:
                image_path = input("Enter the image path: ")
                text = input("Enter the text to hide: ")
                output_path = input("Enter the output image path: ")
                hide_text_in_image(image_path, text, output_path)
            case 11:
                image_path = input("Enter the image path: ")
                print(f"Revealed text: {reveal_text_in_image(image_path)}")
            case 12:
                cover_image_path = input("Enter the cover image path: ")
                secret_image_path = input("Enter the secret image path: ")
                output_path = input("Enter the output image path: ")
                hide_image_in_image(cover_image_path, secret_image_path, output_path)
            case 13:
                image_path = input("Enter the image path: ")
                output_path = input("Enter the output image path: ")
                reveal_image_in_image(image_path, output_path)
            case 14:
                image_path = input("Enter the image path: ")
                data = input("Enter the data to hide: ").encode()
                output_path = input("Enter the output image path: ")
                hide_data_in_image(image_path, data, output_path)
            case 15:
                image_path = input("Enter the image path: ")
                print(f"Revealed data: {reveal_data_in_image(image_path)}")
            case 16:
                usr_input: str = input("Enter the path for the directory")
                file_sort1(usr_input)
            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
