import sys

def check_and_fix_png_signature(file_path):
    # 16-byte header yang akan dicek (8-byte PNG signature + 8-byte tambahan)
    png_header_16 = b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A' + b'\x00\x00\x00\x0D\x49\x48\x44\x52'
    png_footer = b'\x49\x45\x4E\x44\xAE\x42\x60\x82'  # Standard PNG footer

    try:
        with open(file_path, 'rb') as file:
            data = file.read()
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return

    # Check the first 16 bytes of the file (extended header)
    file_header = data[:16]
    if file_header == png_header_16:
        print("Header is correct.")
    else:
        print("Header is incorrect, fixing...")
        data = png_header_16 + data[16:]

    # Check the footer (last 8 bytes)
    file_footer = data[-8:]
    if file_footer == png_footer:
        print("Footer is correct.")
    else:
        print("Footer is incorrect, fixing...")
        data = data[:-8] + png_footer

    # Save the corrected file
    with open(file_path, 'wb') as file:
        file.write(data)

    print(f"File '{file_path}' signature check and correction complete.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 pngfix.py <file.png>")
        sys.exit(1)

    # Take the file name from the command-line argument
    file_name = sys.argv[1]
    check_and_fix_png_signature(file_name)
