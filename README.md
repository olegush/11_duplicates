# Anti-Duplicator

The script finds file duplicates in the given directory and all its subdirectories

# Quickstart

Run **duplicates.py** with  path to root directory as parameter. 

Example of script launch on Linux, Python 3.5:

```bash

$ python duplicates.py <root directory>

Founded duplicates:
index.html (5013 bytes) in tipped
style.css (3852 bytes) in tipped
tipped2.js (75392 bytes) in tipped
tipped2.js (75392 bytes) in tipped/css/tipped2
index.html (5013 bytes) in tipped/css/tipped2/21
index.html (5013 bytes) in tipped/example
tipped2.js (75392 bytes) in tipped/example
style.css (3852 bytes) in tipped/example/css

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
