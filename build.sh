#!/bin/bash
REPO_NAME="static-website"
python3 src/main.py "/${REPO_NAME}/"
echo "Site built successfully with basepath /${REPO_NAME}/"