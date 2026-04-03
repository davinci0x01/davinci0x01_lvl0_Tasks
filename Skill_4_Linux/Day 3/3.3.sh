#!/bin/bash
# Day 3 - Task 3: Kill process by its name

echo "##### Starting apache2 #####"
service apache2 start

echo "##### Checking process IDS ######"
echo "PIDs: $(pgrep apache2 | tr '\n' ' ')"

echo "##### Killing apache2 process #####"
sudo pkill apache2 && echo "apache2 has been successfully terminated"
