#
# 문제 2.
def solution(s):
    answer =0
    r_len =1
    s_list = [1]*len(s)
    for s_idx in range(1, len(s)):
        if s[s_idx] == s[s_idx%r_len]:
            if (s_idx+1)%r_len == 0:
                s_list[s_idx] = r_len
            else:
                s_list[s_idx] = s_idx+1
        else:
            r_len = s_idx+1
            s_list[s_idx] = s_idx+1
    return s_list[-1]

print(solution('abcabcabd'))
print(solution('0045662100456621004566210045662100456621'))


