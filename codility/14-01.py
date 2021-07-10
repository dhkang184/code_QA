# 12:35~

def chk(a, c, s):
    ts = 0  # temp sum
    tc = 0  # temp cnt

    for e in a:
        if ts + e > s:
            ts = e
            tc += 1
        else:
            ts += e
        if tc >= c:
            return False

    return True


def bs(a, k):
    n = len(a)
    small_v = max(a)  # smallest value
    max_u = sum(a)  # max value

    if k == 1: return max_u
    if k >= n: return small_v

    while small_v <= max_u:
        new_v = (small_v + max_u) // 2  # new value
        if chk(a, k, new_v):
            max_u = new_v - 1
        else:
            small_v = new_v + 1

    return small_v


def solution(k, m, a):
    return bs(a, k)

solution(3, 5, [2, 1, 5, 1, 2, 2, 2])