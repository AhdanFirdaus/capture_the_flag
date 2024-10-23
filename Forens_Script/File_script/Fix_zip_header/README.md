# ZIP Header Fixer and Recursive Extractor

This bash script is designed to fix the first 5 bytes of a corrupted ZIP file's header, rename it, and recursively extract the contents. If nested ZIP files are found, it will continue to fix and extract them.

## Features
- Fixes the first 5 bytes of the ZIP header to the correct values (`50 4B 03 04 14`).
- Recursively extracts ZIP files.
- If non-ZIP files are extracted, their contents are printed to the terminal.
- Cleans up temporary files after execution.

## How to Use

1. Make the script executable:
    ```bash
    chmod +x fix_zip.sh
    ```

2. Run the script with the following command:
    ```bash
    ./fix_zip.sh <zip-file>
    ```

    Replace `<zip-file>` with the path to the ZIP file you want to fix and extract.

### Example

To fix and extract a ZIP file named `corrupt.zip`, use the following command:

```bash
./fix_zip.sh corrupt.zip
