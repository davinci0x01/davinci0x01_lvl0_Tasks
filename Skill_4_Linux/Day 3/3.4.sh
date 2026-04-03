#!/bin/bash

process="apache2"

echo "##### Starting $process #####"
service $process start

echo "##### Memory Usage of $process #####"
ps -o pid,%mem,cmd -C $process

echo "##### Stopping $process #####"
service $process stop