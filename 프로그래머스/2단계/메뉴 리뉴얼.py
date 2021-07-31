#https://programmers.co.kr/learn/courses/30/lessons/72411
from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    answer = []
    ans_dict = defaultdict(int)
    count_dict = defaultdict(int)

    for o in orders:
        for l in course:
            if l <= len(o):
                com_list = list(combinations(sorted(o), l))
                for c in com_list:
                    ans_dict[''.join(c)] += 1
                    count_dict[l] = max(ans_dict[''.join(c)], count_dict[l])

    for A in ans_dict.keys():
        if ans_dict[A] >1 and ans_dict[A] == count_dict[len(A)]:
            answer.append(A)

    return sorted(answer)

print(solution(	["XYZ", "XWY", "WXA"], [2, 3, 4]))