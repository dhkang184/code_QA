#
def solution1(n):
    answer = 0
    n_list =[]
    a, b, c = 2, 0, 1
    for x in range(1,n+1):
        if x%4 ==0:
            b = a*(a+1)*(a+2)
            n_list.append(b)
            b =0
            a +=1
        else:
            n_list.append(c*(c+1))
            c +=1
    return n_list[-1]

#print(solution1(4))
def solution(s):
    answer =0
    s_list =[0] *len(s)
    r_len =1
    c_i =0

    while r_len <= len(s):
        r_s = s[:r_len]
        for i in range(r_len,len(s)):
            if s[i] != s[c_i + i%r_len]:
                c_i =0
                r_len +=1
                end_v = False
                break
        if end_v:
            return r_len
    return len(s)

print(solution('abcabcabd'))

