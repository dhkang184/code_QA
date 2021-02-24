#https://www.acmicpc.net/workbook/view/1152
# 시작 시간: 2021.02.24..20:45 종료 시간: 22:00

n = int(input())

new_map = [[0]*(n+1) for _ in range(n+1)]
for r_ in range(n):
    r_input = list(map(int, input().split()))
    for c_ in range(n):
        new_map[r_+1][c_+1] = r_input[c_]

# d1,d2 >= 1, 1<=x<x+d1+d2<=n, 1<=y-d1<y<y+d2<=n

ans_list = [] #x,y,d1,d2


def count_map(ans_):

    x = ans_[0]
    y = ans_[1]
    d1 = ans_[2]
    d2 = ans_[3]

    ans_map = [[0]*(n+1) for _ in range(n+1)]
    ans_count = [0,0,0,0,0] #선거구역 합
    num = 0
    for i1 in range(d1+1):
        ans_map[x+i1][y-i1] = 5
        ans_map[x+d2 +i1][y+d2-i1] =5
    for i2 in range(d2+1):
        ans_map[x+i2][y+i2] = 5
        ans_map[x+d1 +i2][y-d1 + i2] = 5

    for j in range(x+1, x+d1+d2):
        s_idx = 0
        for k in range(n+1):
            if ans_map[j][k] ==5 and s_idx ==0:
                s_idx =1
            elif ans_map[j][k] ==5 and s_idx ==1:
                s_idx =0
            if s_idx == 1:
                ans_map[j][k] =5


    for r_ in range(1,n+1):
        for c_ in range(1,n+1):
            if ans_map[r_][c_] ==5:
                num =4
            elif r_ <x+d1 and c_ <=y:
                num =0
            elif r_<=x+d2 and y<c_<=n:
                num = 1
            elif x+d1 <=r_<=n and c_ <y-d1+d2:
                num = 2
            elif x+d2 < r_ <=n and y-d1+d2 <=c_ <= n:
                num =3

            ans_count[num] += new_map[r_][c_]

    ans_count.sort()

    return ans_count[-1] - ans_count[0]


for x in range(1, n+1):
    for y in range(2, n+1):
        for d1 in range(1, n):
            for d2 in range(1,n):
                if x +d1 +d2 <=n and 1<=y-d1 and y+d2<=n:
                    ans_list.append((x,y,d1,d2))
answer = 1e9
count_map((3,3,1,1))
for x in ans_list:
    answer = min(count_map(x), answer)
    if answer == 0:
        break

print(answer)



