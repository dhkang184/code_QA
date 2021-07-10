#https://app.codility.com/c/run/training2V96SA-7U3/
# 24:05~ 24:10

def solution(X, Y, D):
    # write your code in Python 3.6
    answer = 0
    if (Y-X)%D ==0:
        answer = (Y-X)//D
    else:
        answer = 1+ (Y-X)//D
    return answer