#!/usr/bin/env python
import time
while 1:
    s = 'это бегущая заглавная буква по строке'
    i = 1
    while i < s.__len__()+1:
        print(s[:i-1]+ (s[i-1:i]).upper() + s[i:]+'\r', end='', flush=True)
        time.sleep(0.2)
        i = i + 1
