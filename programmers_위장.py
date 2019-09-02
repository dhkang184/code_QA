def solution(clothes):
    answer = 0
    parts = {}
    for item in clothes:
        if item[-1] in parts:
            parts[item[-1]] += 1
        else:
            parts[item[-1]] = 1
    #for key, val in parts.items():
    prop = 1
    for val in parts.values():
        prop *= (val+1)
    answer = prop -1


    return answer