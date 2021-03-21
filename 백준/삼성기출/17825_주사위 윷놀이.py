#https://www.acmicpc.net/problem/17825
#시작시간: 18:40

from collections import deque

data = list(map(int,input().split()))
score_list = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,0,
            13,16,19,25,30,35,22,24,28,27,26,]
# 25: 가운데 25점
# 5 ->22,10 ->28, ,15 ->30 번으로 이동
# 21 : 도착
# 29 -> 25
# 32 -> 25
# 27 ->20

move_dict = {5: [22,23,24,25,26,27],
             10: [28,29,25,26,27,20],
             15: [30,31,32,25,26,27],
             22: [23,24,25,26,27,20],
             23: [24,25,26,27,20,21],
             24: [25,26,27,20,21,21],
             25: [26,27,20,21,21,21],
             26: [27,20,21,21,21,21],
             27: [20,21,21,21,21,21],
             28: [29,25,26,27,20,21],
             29: [25,26,27,20,21,21],
             30: [31,32,25,26,27,20],
             31: [32,25,26,27,20,21],
             32: [25,26,27,20,21,21]
             }



que = deque()
score = score_list[data[0]]
temp = [data[0],0,0,0]
que.append((temp,1, score))


while que:
    temp, step, c_score = que.popleft()

    # if step == 10:
    #     que.append((temp, step))
    #     break
    for x in range(4):
        c = temp[x]
        if c != 21:

            if c in move_dict:
                n_c = move_dict[c][data[step] - 1]
            else:
                n_c = c + data[step]
                if n_c > 21:
                    n_c = 21

            if n_c == 21 or n_c not in temp:
                n_temp = []
                for y in range(4):
                    if y == x:
                        n_temp.append(n_c)
                    else:
                        n_temp.append(temp[y])

                if step == 9:
                    n_score = c_score + score_list[n_c]
                    score = max(score, n_score)
                else:
                    n_score = c_score + score_list[n_c]
                    que.append((n_temp, step+1, n_score))

print(score)
