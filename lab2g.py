#!/usr/bin/env python3

#Author: Rajib Khan
#Author ID: rkhan2
#Date Created: 2020/01/21

import sys

if len(sys.argv) == 1:
    timer = 3

else: 

    timer = int(sys.argv[1])

while timer > 0:
    print(timer)
    timer = timer - 1
print('blast off!')
