#!/bin/bash

service apache2 start

echo "PIDs: $(pgrep apache2 | tr '\n' ' ')"

service apache2 stop