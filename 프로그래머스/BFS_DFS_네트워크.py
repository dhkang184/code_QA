#https://programmers.co.kr/learn/courses/30/lessons/43162
# 시작시간: 00:35~ 1:10

def solution(n, computers):
    answer = 0
    ans_list = [i+1 for i in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] ==1:
                i_n =ans_list[i]
                j_n =ans_list[j]
                if i_n > j_n:
                    for x in range(n):
                        if ans_list[x] == i_n:
                            ans_list[x] = j_n
                elif i_n < j_n:
                    for x in range(n):
                        if ans_list[x] ==j_n:
                            ans_list[x] = i_n

    answer = len(list(set(ans_list)))

    return answer

"""
def solution(n, computers):
    temp = []
    for i in range(n):
        temp.append(i)
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                for k in range(n):
                    if temp[k] == temp[i]:
                        temp[k] = temp[j]
    return len(set(temp))
"""


print((solution(3,	[[1, 1, 0], [1, 1, 0], [0, 0, 1]] )))