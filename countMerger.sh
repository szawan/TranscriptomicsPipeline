#!/bin/bash

# Check if a directory path is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <directory_path>"
    exit 1
fi
# Set the directory path
directory_path="$1"

# Get the list of files in the directory
files=("$directory_path"/*)

# Extract the second column from each file and add as a new column to the first file
for ((i=1; i<${#files[@]}; i++)); do
    awk -v OFS='\t' 'FNR==NR{a[NR]=$2; next} {print $0, a[FNR]}' "${files[$i]}" "${files[0]}" > temp_file && mv temp_file "${files[0]}"
done