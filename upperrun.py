#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
while 1:
    s = 'привет как дела'
    i = 1
    f = 'u'
    while i < s.__len__()+1:
        print(s[:i-1]+ (s[i-1:i]).upper() + s[i:]+'\r', end='', flush=True)
        time.sleep(0.2)
        i = i + 1
