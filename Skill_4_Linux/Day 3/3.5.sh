#!/bin/bash

echo "##### Top 5 Processes by CPU Usage #####"
ps aux --sort=-%cpu | head -n 6