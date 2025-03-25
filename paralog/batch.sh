#!/bin/bash

work_path="/BiO/Live/rooter/Downloads/supplement/paralog"

cd $work_path

list_file="/BiO/Live/rooter/Downloads/ortholog/list_copy.csv"

# Read the CSV file line by line
while IFS=, read -r -a row; do
  # Loop through each variable in the row
  for variable in "${row[@]}"; do
    # Run the launch command in the background
    python main.py --var $variable &
  done
done < "$list_file"

# Wait for all background jobs to complete
wait
