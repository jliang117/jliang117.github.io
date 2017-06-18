#!/bin/sh
cd "C:\Users\Jimmy\Desktop\jim's files\sampleSalePython\gitPage\jliang117.github.io"
pwd
python scrape.py
sleep 5
git add .
git commit -m "updated Json"
git push
echo Press Enter...
read
