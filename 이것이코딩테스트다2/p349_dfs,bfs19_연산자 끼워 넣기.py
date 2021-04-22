#https://www.acmicpc.net/problem/14888
# 22:00~

n = int(input())
num_list = list(map(int, input().split()))
data = list(map(int, input().split())) #+,-,x,/

def div(a ,b):
    if a<0:
        return(-((-a)//b))
    else:
        return a//b
from collections import deque

Q = deque([(num_list[0], data)])

for next_num in num_list[1:]:
    Q_len = len(Q)
    for step in range(Q_len):
        num, c_data = Q.popleft()
        for data_idx in range(4):
            if c_data[data_idx] >0:
                next_data = [d for d in c_data]
                next_data[data_idx] -= 1
                if data_idx ==0:
                    Q.append((num + next_num, next_data ))
                elif data_idx ==1:
                    Q.append((num - next_num, next_data))
                elif data_idx ==2:
                    Q.append((num * next_num, next_data))
                elif data_idx ==3:
                    Q.append((div(num, next_num), next_data))

print(max(Q)[0])
print(min(Q)[0])
