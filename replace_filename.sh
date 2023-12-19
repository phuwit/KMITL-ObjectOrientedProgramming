#!/bin/bash

# Navigate to the root directory
cd .

# Use find command to get all files
files=$(find . -type f)

# Use for loop to iterate over each file
for file in $files
do
    # Use mv command to rename the file, replacing - with _ and : with __
    newfile=$(echo $file | tr '-' '_' | tr ':' '__')
    mv "$file" "$newfile"
done