import sys

def check_and_fix_jpeg_signature(file_path):
    # 12-byte header yang akan dicek (biasanya terdiri dari SOI marker dan APP0 marker)
    jpeg_header_12 = b'\xFF\xD8\xFF\xE0\x00\x10\x4A\x46\x49\x46\x00\x01'
    jpeg_footer = b'\xFF\xD9'  # Standard JPEG footer (End of Image marker)

    try:
        with open(file_path, 'rb') as file:
            data = file.read()
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return

    # Check the first 12 bytes of the file (extended header)
    file_header = data[:12]
    if file_header == jpeg_header_12:
        print("Header is correct.")
    else:
        print("Header is incorrect, fixing...")
        data = jpeg_header_12 + data[12:]

    # Check the footer (last 2 bytes)
    file_footer = data[-2:]
    if file_footer == jpeg_footer:
        print("Footer is correct.")
    else:
        print("Footer is incorrect, fixing...")
        data = data[:-2] + jpeg_footer

    # Save the corrected file
    with open(file_path, 'wb') as file:
        file.write(data)

    print(f"File '{file_path}' signature check and correction complete.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 jpegfix.py <file.jpg>")
        sys.exit(1)

    # Take the file name from the command-line argument
    file_name = sys.argv[1]
    check_and_fix_jpeg_signature(file_name)