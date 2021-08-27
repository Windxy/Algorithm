#!/usr/bin/env python
# coding=utf-8
# https://discuss.acmcoder.com/topic/5d81deac9b427acc0bcee2ed
# 例题：a+b
while 1:
    a = []
    s = input()
    # S = list(map(int,input().split()))
    if s != "":
        for x in s.split():
            a.append(int(x))

        print(sum(a))
    else:
        break