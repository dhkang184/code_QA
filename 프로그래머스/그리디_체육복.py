#https://programmers.co.kr/learn/courses/30/lessons/42862
#24:25~

def solution(n, lost, reserve):
    answer = 0
    v_list = [1] * (n+1)
    v_list[0] = 0

    for x in lost:
        v_list[x] = 0

    for y in reserve:
        v_list[y] += 1

    for x in range(1, n+1):
        if x == 1 and v_list[x] ==0 and v_list[x+1] == 2:
            v_list[0] =1
            v_list[1] -=1
        elif x == n and v_list[x] ==0 and v_list[x-1] == 2:
            v_list[x] += 1
            v_list[x-1] -= 1
        elif 1<x<n and v_list[x] == 0:
            if v_list[x-1] == 2:
                v_list[x] +=1
                v_list[x-1] -= 1
            elif v_list[x+1] ==2:
                v_list[x] +=1
                v_list[x+1] -=1

    for x in range(1, n+1):
        if v_list[x] != 0:
            answer += 1
    return answer

print(solution(5,[2,4],[3]))