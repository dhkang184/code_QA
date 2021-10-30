#https://www.acmicpc.net/problem/1920

N = int(input())
A = sorted(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

def binary(l, A, start, end):
    if start > end:
        return 0
    m = (start + end)//2
    if l == A[m]:
        return 1
    elif l< A[m]:
        return binary(l, A, start, m-1)
    else:
        return binary(l, A, m+1, end)

for m in M_list:
    print(binary(m, A, 0, N-1))