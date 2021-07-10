#https://app.codility.com/c/run/trainingVQHW3N-Q62/
# 22:25 ~ 22:30

def solution(N):
    # write your code in Python 3.6
    B = str(format(N, 'b'))
    max_v = 0
    c_v = 0
    check_v = False # True: 0 이어짐
    for b in B:
        if check_v == False and b =='0':
            c_v = 1
            check_v = True
        elif check_v == True and b =='0':
            c_v +=1
        elif check_v == True and b =='1':
            max_v = max(max_v, c_v)
            c_v =0

    return max_v
