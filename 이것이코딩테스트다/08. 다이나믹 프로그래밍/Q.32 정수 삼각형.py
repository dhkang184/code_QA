#https://www.acmicpc.net/problem/1932

n = int(input())

data = [list(map(int, input().split())) for _ in range(n)]

sum_list =[0]*n
sum_list[0] = data[0][0]

for y in range(1, len(data)):
    last_sum_list = [l for l in sum_list ]
    for z in range(len(data[y])):
        if z == 0:
            sum_list[z] = data[y][z] + last_sum_list[z]
        elif z == len(data[y]) -1 :
            sum_list[z] =data[y][z] + last_sum_list[z-1]
        else:
            sum_list[z] = data[y][z] +max(last_sum_list[z-1], last_sum_list[z])

print(max(sum_list))
