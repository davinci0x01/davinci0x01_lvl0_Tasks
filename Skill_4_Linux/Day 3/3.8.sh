#!/bin/bash

service_name="NetworkManager"

echo "##### Restarting $service_name #####"
sudo systemctl restart $service_name

sleep 2

echo "##### Checking PID after restart #####"
echo "PIDs: $(pgrep $service_name | tr '\n' ' ')"