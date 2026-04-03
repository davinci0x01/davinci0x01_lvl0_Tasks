#!/bin/bash

if [[ "$(uname)" == "Linux" ]]; then
    echo "The system is running Linux."
else
    echo "The system is NOT running Linux."
fi