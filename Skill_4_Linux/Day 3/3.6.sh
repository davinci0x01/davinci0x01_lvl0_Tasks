#!/bin/bash

service_name="apache2"

echo "##### Starting $service_name using systemctl #####"
sudo systemctl start $service_name


echo "##### Checking PID #####"
echo "PIDs: $(pgrep $service_name | tr '\n' ' ')"

