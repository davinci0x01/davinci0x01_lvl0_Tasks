#!/bin/bash

echo "Hostname: $(hostname)"
echo "Local IP: $(hostname -I | awk '{print $1}')"