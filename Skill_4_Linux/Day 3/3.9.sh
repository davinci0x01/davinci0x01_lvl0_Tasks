#!/bin/bash

service_name="apache2"

echo "##### Showing last 20 logs for $service_name #####"

sudo journalctl -u $service_name -n 20 --no-pager