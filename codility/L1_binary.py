#https://app.codility.com/c/run/trainingHVE7TH-487/

#22:25 ~ 22~30

def solution(N):
    # write your code in Python 3.6
    B = str(bin(N))[2:]
    answer = 0
    temp =0
    for x in B:
        if x == '0':
            temp +=1
        else:
            answer = max(answer, temp)
            temp =0
    return answer
    pass

print(solution(1041))