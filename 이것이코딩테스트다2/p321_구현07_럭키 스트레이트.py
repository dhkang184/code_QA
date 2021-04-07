#https://www.acmicpc.net/problem/18406
# 12:20~ 12:25

d = input()
data = [int(x) for x in d]

if sum(data[:len(data)//2]) == sum(data[len(data)//2:]):
    print("LUCKY")
else:
    print("READY")
