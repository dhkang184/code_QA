#24:50~ 01:00
# https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/
def solution(X, A):
    X_list = [0]* X
    for a_idx, a in enumerate(A):
        if X_list[a-1] == 0:
            X -= 1
            X_list[a-1] =1
            if X ==0:
                return a_idx
    return -1