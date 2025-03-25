#!/bin/bash

work_path="/BiO/Live/rooter/Downloads/supplement/scoring"

cd $work_path

list_file="/BiO/Live/rooter/Downloads/zzzz.csv"

# Read the CSV file line by line
while IFS=, read -r -a row; do
  # Loop through each variable in the row
  for variable in "${row[@]}"; do
    # Run the launch command in the background
    echo $variable
    python supplementary.py -var $variable &
  done
done < "$list_file"

# Wait for all background jobs to complete
wait

echo "All done!"
