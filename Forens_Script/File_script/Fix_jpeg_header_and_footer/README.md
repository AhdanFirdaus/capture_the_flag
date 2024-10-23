# JPEG Signature Checker and Fixer

This Python script checks and fixes the signature (header and footer) of a JPEG file. It ensures that the first 12 bytes of the file (header) and the last 2 bytes (footer) conform to the JPEG format specification.

## Features
- Checks the first 12 bytes of the JPEG file (SOI and APP0 markers).
- Checks the last 2 bytes of the JPEG file (EOI marker).
- Automatically fixes any incorrect signatures or footers.
- Overwrites the file with the corrected data.

## Prerequisites
- Python 3.x installed on your system.

## How to Use

1. Run the script with the following command:
    ```bash
    python3 jpegfix.py <file.jpg>
    ```

    Replace `<file.jpg>` with the path to the JPEG file you want to check and fix.

### Example

To check and fix the signature of a JPEG file named `photo.jpg`, use the following command:

```bash
python3 jpegfix.py photo.jpg
