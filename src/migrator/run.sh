#!/bin/sh
echo "Running main.py every 5 minutes";

while true; do
    echo "Executing main.py at $(date)"
    python main.py
    sleep 300
done
