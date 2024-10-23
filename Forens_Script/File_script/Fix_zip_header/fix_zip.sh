#!/bin/bash

# Function to fix the ZIP header, rename to 100.zip, and print contents of the final file
fix_and_rename_zip() {
    local zip_file="$1"
    local output_dir="$2"

    # Fix the first 5 bytes of the ZIP header to 50 4B 03 04 14
    printf '\x50\x4B\x03\x04\x14' | dd of="$zip_file" bs=1 count=5 conv=notrunc 2>/dev/null
    
    # Unzip the file to a temporary directory
    temp_dir=$(mktemp -d)
    unzip -q "$zip_file" -d "$temp_dir"

    # Rename and move the extracted ZIP file(s) to output_dir
    for file in "$temp_dir"/*; do
        if [ -f "$file" ]; then
            if file "$file" | grep -q "Zip archive data"; then
                mv "$file" "$output_dir/100.zip"
                fix_and_rename_zip "$output_dir/100.zip" "$output_dir"
            else
                # If the extracted file is not a ZIP, move it and print its contents
                mv "$file" "$output_dir/"
                echo "Extracted: $output_dir/$(basename "$file")"
                echo "Contents of $(basename "$file"):"
                cat "$output_dir/$(basename "$file")"
            fi
        fi
    done

    # Clean up the temporary directory
    rm -rf "$temp_dir"
}

# Main script execution
if [ -z "$1" ]; then
    echo "Usage: $0 <zip-file>"
    exit 1
fi

# Set the initial output directory (current directory)
initial_output_dir=$(pwd)
mv "$1" "$initial_output_dir/100.zip"
fix_and_rename_zip "$initial_output_dir/100.zip" "$initial_output_dir"
