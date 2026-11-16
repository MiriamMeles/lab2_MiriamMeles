#!/bin/bash

# If the archive folder does not exist, create it
if [ ! -d "archive" ]; then
    mkdir archive
    echo "Archive folder created."
fi

# Get the current date and time
timestamp=$(date +"%Y%m%d-%H%M%S")

# Archive grades.csv if it exists and rename it
if [ -f "grades.csv" ]; then
    new_name="grades_${timestamp}.csv"
    mv grades.csv "archive/$new_name"
    touch grades.csv
    echo "$timestamp | grades.csv -> $new_name" >> organizer.log
    echo "Archived as $new_name"
else
    echo "Error: grades.csv not found. Nothing to archive."
    exit 1
fi