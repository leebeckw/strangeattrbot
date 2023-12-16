#!/bin/bash

python3 gen_img_for_gh.py

# Navigate to the directory of your Git repository
cd /strangeattrbot

# Add all changes to the staging area
git add .

# Commit changes with a message
git commit -m "new image"

# Push changes to the default branch (e.g., master)
git push