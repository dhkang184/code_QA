# 01:00~01:30
#https://app.codility.com/c/run/training2Z5XUJ-Y5V/

def solution(N, A):
    N_list = [0]*N
    next_max =0
    current_max =0
    for a in A:
        if a == N+1:
            current_max = next_max
        else:
            next_max = max(next_max,max(N_list[a-1], current_max) +1)
            N_list[a-1] = max(N_list[a-1], current_max) +1

    answer = []
    for n in N_list:
        if n >= current_max:
            answer.append(n)
        else:
            answer.append(current_max)

    return answer