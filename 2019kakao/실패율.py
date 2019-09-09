# https://www.welcomekakao.com/learn/courses/30/lessons/42889

def solution(N, stages):
    answer = []

    stages.sort()
    error_dict ={}
    for err_idx in range(N):
        error = 0.0
        if err_idx+1 in stages:
            fail_num = stages.count(err_idx+1)
            stage_total_user = len(stages[stages.index(err_idx +1):])
            error = fail_num/stage_total_user
        if error in error_dict:
            error_dict[error].append(err_idx + 1)
        else:
            error_dict[error] = [err_idx + 1]
    for ans in sorted(error_dict, reverse=True):
        for y in error_dict[ans]:
            answer.append(y)
    print(answer)
    return answer

stages = [2, 1, 2, 6, 2, 4, 3, 3]
N = 5
# stages=[4,4,4]
# N =5
solution(N, stages)