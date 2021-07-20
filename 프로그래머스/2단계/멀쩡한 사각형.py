# https://programmers.co.kr/learn/courses/30/lessons/62048
from math import gcd  #최대공약수 gcd(12,8) -> 4

def solution(w,h):
    answer = 1
    g = gcd(w,h)
    answer = w*h - (g* (w//g + h//g -1))

    return answer