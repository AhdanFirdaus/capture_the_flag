# PNG Signature Checker and Fixer

This Python script checks and fixes the signature (header and footer) of a PNG file. It ensures that the first 16 bytes of the file (header) and the last 8 bytes (footer) conform to the PNG format specification.

## Features
- Checks the first 16 bytes of the PNG file (signature and IHDR chunk).
- Checks the last 8 bytes of the PNG file (IEND chunk and CRC).
- Automatically fixes any incorrect signatures or footers.
- Overwrites the file with the corrected data.

## Prerequisites
- Python 3.x installed on your system.

## How to Use

1. Run the script with the following command:
    ```bash
    python3 pngfix.py <file.png>
    ```

    Replace `<file.png>` with the path to the PNG file you want to check and fix.

### Example

To check and fix the signature of a PNG file named `image.png`, use the following command:

```bash
python3 pngfix.py image.png
