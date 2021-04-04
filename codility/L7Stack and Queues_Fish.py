#https://app.codility.com/c/run/training9YWJ2R-8YW/
# 22:45~ 23:08

def solution(A, B):
# A: 크기
# B: 방향- 0: 위, 1: 아래
    up_list = []
    down_list =[]
    for a,b in zip(A,B):
        if b == 0:
            if len(down_list) ==0:
                up_list.append(a)
            else:
                while True:
                    if len(down_list) ==0:
                        up_list.append(a)
                        break
                    elif down_list[-1] > a:
                        break
                    elif down_list[-1] <a:
                        down_list.pop()
        else:
            down_list.append(a)

    return len(up_list) + len(down_list)

    pass

print(solution([4,3,2,1,5], [1,0,1,1,1]))