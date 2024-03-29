#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 21:49:17 2021

@author: harry
"""

from datetime import *

today = datetime.today()
print('Today is: ', today)

for attr in \
    ['year','month','day','hour','minute','second','microsecond'] :
        print(attr , '\t' , getattr(today , attr))
        
print('Time: ', today.hour , ':' , today.minute, sep = '')

day = today.strftime('%A')
month = today.strftime('%B')

print('Date: ' , day , month , today.day)
