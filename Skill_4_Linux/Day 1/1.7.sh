#!/bin/bash

lscpu | grep "Model name" | xargs

echo "Number of CPU Cores: $(nproc)"
