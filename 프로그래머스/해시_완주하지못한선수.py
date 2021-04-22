#https://programmers.co.kr/learn/courses/30/lessons/42576
# 시작시간: 22:30 종료 시간: 22:35
def solution(participant, completion):
    sort_p = sorted(participant)
    sort_c = sorted(completion)
    for idx, p in enumerate(sort_p):
        if p != sort_c[idx]:
            return p

