#완주하지 못한선수 - https://programmers.co.kr/learn/courses/30/lessons/42576
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for idx in range(len(participant)):
        if participant[idx] != completion[idx]:
            break

    # 효용성 떨어지는 코드.....
    # for part in completion:
    #     if part in participant:
    #         pop_index = participant.index(part)
    #         participant.pop(pop_index)

    answer = participant[idx]
    return answer