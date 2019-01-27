#!/bin/sh

sudo apt-get update
sudo apt-get install python3.6

xtract the tarball
tar xvfz Python-3.5.1.tgz
Configure and Install:
cd Python-3.5.1
./configure --prefix = /opt/python3.5.1
make  
sudo make install

python project.py
