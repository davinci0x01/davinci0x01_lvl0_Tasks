#!/bin/bash

file1="hello.txt"
file2="file.txt"
file3="test-file.txt"

echo "##### $file1 to $file2 #####"
diff "$file1" "$file2"

echo "##### $file1 to $file3 #####"
diff "$file1" "$file3"
