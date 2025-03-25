#!/bin/bash

work_path="/BiO/Live/rooter/Downloads/supplement/scoring/Gr_unanalyzed"

cd $work_path

dest="/BiO/Live/rooter/Downloads/supplement/scoring/Gr_unanalyzed/A_summary/"

  # 使用 for 循环遍历文件夹下的所有文件
for dir in *; do
    if [ -d "$dir" ] && [ "$dir" != "A-index" ]; then
        # echo "$dir" >> "$dest"$dir"_index.csv"
        echo "$dest"$dir"_index.csv"
        mkdir -p "$dest"
        cd "$dir"
        for file in *; do
          if [ -f "$file" ]; then
            filename_without_ext=$(echo "$file" | sed 's/\.csv$//')
            echo "$filename_without_ext" >> "$dest"$dir"_index.csv"
        #     pwd
            # grep '>' "$file" >> "$work_path/A-index/$dir/$file" &
            awk -F, '$1 ~ /^>/ && $3 ~ /score *= *[1-9]/' "$file" >> "$dest"$dir"_index.csv"
          fi
        done
        cd ..  
    fi
done

# Wait for all background jobs to complete
wait

echo "All done!"
