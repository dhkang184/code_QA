#https://programmers.co.kr/learn/courses/30/lessons/17676
# 15:20~
from collections import defaultdict

def check_f(time, li):
    c = 0
    start = time
    end = time+1000
    for i in li:
        if i[1] >= start and i[0] <end:
            c+=1
    return c

def solution(lines):
    li =[]
    r =1
    for l in lines:
        y, a, b = l.split()
        a = a.split(":")
        b = float(b.replace('s','')) *1000
        end = (int(a[0])*3600 + int(a[1])*60 + float(a[2])) * 1000
        start = end -b +1
        li.append([start, end])
    for i in li:
        r = max(r, check_f(i[0], li), check_f(i[1], li))

    return r