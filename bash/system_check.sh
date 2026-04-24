#!/usr/bin/env bash

date=$(date +%Y-%m-%d)
check_disk=$(command df / | tail -1 | awk '{print $5}' | tr -d '%')
dirs=("/home" "/etc" "/nix" "/fake/dir")

echo "=== System Check ==="
echo "Host: ${HOSTNAME}"
echo "Date: ${date}"

echo "--- Disk ---"

if [ "$check_disk" -ge 90 ]; then 
  echo "WARNING: your disk is ${check_disk}%"
elif [ "$check_disk" -ge 65 ]; then
  echo "CRITICAL: your disk is ${check_disk}%"
else
  echo "OK: your disk is ${check_disk}%"
fi


echo "--- Directories ---"

check_dir() {
  if [ -d "$1"  ]; then
    echo "$1 EXISTS"
  else
    echo "$1 NOT FOUND"
  fi
}

for dir in "${dirs[@]}"; do
  check_dir "$dir"
done

