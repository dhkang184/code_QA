def solution(A):
    # write your code in Python 3.6
    A = list(set(sorted(A)))
    if A[-1] <= 0:
        return 1

    c = 1
    for x in A:
        if x > c:
            return c
        elif x == c:
            c += 1

    return c

print(solution([1, 23, 3, 1, 2, 3, 12, 3, -100, 51, 2, 3, 1, 2, 3, 2, 1, 2, 3, -20]))