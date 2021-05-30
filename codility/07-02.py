# 12:20~12:30

def solution(A,B):
    up_list = []
    down_list = []
    for idx in range(len(A)):
        if B[idx] == 0:
            while True:
                if len(down_list) == 0:
                    up_list.append(A[idx])
                    break
                elif down_list[-1] < A[idx]:
                    down_list.pop()
                elif down_list[-1] > A[idx]:
                    break

        else:
            down_list.append(A[idx])
    return(len(up_list) + len(down_list))