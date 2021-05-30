def solution(S):
    val = 0
    for x in S:
        if x == '(':
            val +=1
        else:
            val -= 1

        if val <0:
            return 0
    if val ==0:
        return 1
    else:
        return 0