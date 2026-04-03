#!/bin/bash

service_name="NetworkManager"
#service_name="apache2"

echo "##### Checking if $service_name is enabled at boot #####"

status=$(systemctl is-enabled $service_name 2>/dev/null)

if [[ "$status" == "enabled" ]]; then
    echo "$service_name is enabled at boot."
elif [[ "$status" == "disabled" ]]; then
    echo "$service_name is disabled at boot."
else
    echo "Service status: $status"
fi