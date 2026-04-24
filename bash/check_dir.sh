#!/usr/bin/env bash 

dirs=("/etc" "/home" "/tmp" "/fake/dir" "/var")

check_dir() {
  if [ -d "$1" ]; then 
    echo "$1 EXISTS"
  else 
    echo "$1 NOT FOUND"
  fi
}

for dir in "${dirs[@]}"; do 
  check_dir "$dir"
done


