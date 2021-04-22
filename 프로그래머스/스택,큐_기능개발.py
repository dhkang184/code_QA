#https://programmers.co.kr/learn/courses/30/lessons/42586
#시작 시간: 17:05

def solution(progresses, speeds):
    answer = []
    ans = 0
    c_time =0
    for i in range(len(progresses)):
        if (100 - progresses[i])%speeds[i] ==0:
            work_day = (100- progresses[i])//speeds[i]
        else:
            work_day = (100- progresses[i])//speeds[i] +1

        if i == 0:
            c_time = work_day

        if work_day > c_time:
            answer.append(ans)

        if work_day <= c_time:
            ans +=1
        else:
            ans = 1
            c_time = work_day
    answer.append(ans)
    return answer

print(solution([93,30,55], [1,30,5]))