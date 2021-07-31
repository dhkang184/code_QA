#https://programmers.co.kr/learn/courses/30/lessons/72412
# 23:10 ~
def solution1(info, query):
    answer = []
    info_list = []
    for i in info:
        info_line = list(i.split(' '))
        info_line[-1] = int(info_line[-1])
        info_list.append(info_line)

    info_list = sorted(info_list, key=lambda x: -x[-1])

    for q in query:
        q_list = list(q.split(' and '))
        last_q = q_list.pop()
        q_food, score = last_q.split(' ')[0], int(last_q.split(' ')[-1])
        q_list.append(q_food)
        q_list.append(score)
        a = 0
        I_end = True
        for _info in info_list:
            if q_list[-1] > _info[-1]:
                answer.append(a)
                I_end = False
                break
            else:
                add_idx = True
                for Q_idx in range(4):
                    if q_list[Q_idx] != "-" and q_list[Q_idx] != _info[Q_idx]:
                        add_idx = False
                        break
                if add_idx:
                    a +=1
        if I_end:
            answer.append(a)

    return answer


def solution(info, query):
    answer = []
    info_list = []
    for i in info:
        info_line = list(i.split(' '))
        info_line[-1] = int(info_line[-1])
        info_list.append(info_line)

    info_list = sorted(info_list, key=lambda x: -x[-1])


    for q in query:
        q = q.replace(' and ', ' ')
        q_list = list(q.split(' '))
        ans_0 = []
        ans_1 = []
        ans_2 = []
        ans_3 =[]
        for

    return answer

#이진 탐색
def binary_search_():
    import bisect




print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
               ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))