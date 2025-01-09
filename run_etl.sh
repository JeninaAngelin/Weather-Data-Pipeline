#!/bin/bash

# This script assumes that extract.py, transform.py, and load.py are in the same directory as this script.

# Set Python interpreter path if needed
PYTHON=python3

# Run extract.py
echo "Running extract.py..."
$PYTHON src/extract.py

# Check if extract.py executed successfully
if [ $? -ne 0 ]; then
  echo "extract.py failed. Exiting."
  exit 1
fi

# Run transform.py
echo "Running transform.py..."
$PYTHON src/transform.py

# Check if transform.py executed successfully
if [ $? -ne 0 ]; then
  echo "transform.py failed. Exiting."
  exit 1
fi

# Run load.py
echo "Running load.py..."
$PYTHON src/load.py

# Check if load.py executed successfully
if [ $? -ne 0 ]; then
  echo "load.py failed. Exiting."
  exit 1
fi

echo "ETL process completed successfully."
