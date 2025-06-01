#!/usr/bin/env python3
'''Lab 3 Inv 2 Part 2 - subprocess free space'''
# Author ID: mgstephenson

import subprocess

def free_space():
    # Run Linux command and return free disk space on root
    p = subprocess.Popen(
        "df -h | grep '/$' | awk '{print $4}'", 
        stdout=subprocess.PIPE, 
        stdin=subprocess.PIPE, 
        stderr=subprocess.PIPE, 
        shell=True
    )
    output = p.communicate()
    return output[0].decode('utf-8').strip()

if __name__ == '__main__':
    print(free_space())
