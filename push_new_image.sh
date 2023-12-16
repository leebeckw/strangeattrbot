#!/bin/bash

python3 gen_img_for_gh.py

# Add all changes to the staging area
git add .

# Commit changes with a message
git commit -m "new image"

# Push changes to the default branch (e.g., master)
git push

sleep 30

python3 strangeattr_arenabot.py