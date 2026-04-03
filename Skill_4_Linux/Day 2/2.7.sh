#!/bin/bash

original="hello.txt"
link="hello_link.txt"

ln -s "$original" "$link"

echo "Symbolic link created successfully."

ls -l "$link"