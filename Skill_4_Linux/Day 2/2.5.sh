#!/bin/bash

user="test"
directory="test_folder"

echo "##### Create $directory and file in it #####"
mkdir $directory
touch $directory/test_file.txt
echo "Done"

echo "##### Create User #####"
sudo adduser $user

sudo chown -R $user:$user $directory

echo "Ownership changed successfully."

ls -lah $directory

echo "##### Delete user #####"
sudo userdel -r $user
echo "User Deleted"

echo "##### Delete folder #####"
sudo rm -rf $directory
echo "Folder deleted"