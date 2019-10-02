#https://app.codility.com/programmers/lessons/1-iterations/binary_gap/
def solution(N):
    # write your code in Python 3.6
    binary_N = str(bin(N)[3:])
    max_len = 0
    while '1' in binary_N:
        if '1' in binary_N:
            n_idx = binary_N.index('1')
            new_len = n_idx
            binary_N = binary_N[n_idx+1:]
            if new_len > max_len:
                max_len = new_len
    return int(max_len)
    pass