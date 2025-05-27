#!/bin/bash
echo "Installing BCF WEB CRASH dependencies..."
pkg install python -y
pip install requests colorama
echo "Done!"
echo "To run: python bcf-web-crash.py"
