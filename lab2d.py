#!/usr/bin/env python3

import sys

if len(sys.argv) != 3 or len(sys.argv) == 1:
    print('Usage: ./lab2d.py name age')
    sys.exit()    

name = sys.argv[1]
age = sys.argv[2]


print('Hi ' + name + ', you are ' + str(age) + ' years old.')

