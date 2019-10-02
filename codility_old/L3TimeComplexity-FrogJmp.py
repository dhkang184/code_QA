#https://app.codility.com/c/run/training34AYYS-VKE/
def solution(X, Y, D):
    # write your code in Python 3.6
    yd = Y-X
    jumps = yd/D
    if jumps%1 == 0:
        return int(jumps)
    else:
        return int(jumps) +1
    pass
