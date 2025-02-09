#!/usr/bin/env bash
# usage: ./add-lastmod.sh directory-name
directory="$1"
files=$(find "$directory" -type f)
for file in $files; do
  echo "${file}"
  lastmod_date=$(git log --no-show-signature -1 --format=%aI "$file") # example: 2024-05-16T14:23:53+08:00
  echo "$lastmod_date"
  # Use awk to insert the lastmod line above the second ---
  awk -v lastmod="lastmod: $lastmod_date # remove this line if the content is actually changed" '
  BEGIN { frontmatter = 0 }
  /^---$/ { frontmatter++ }
  frontmatter == 2 && !printed { print lastmod; printed = 1 }
  { print }
  ' "$file" >tmpfile && mv tmpfile "$file"
done
