def solution1(A, B):
    # write your code in Python 3.6
    answer = 0

    card_rank = "2 3 4 5 6 7 8 9 10 J Q K A"
    rank_list = [r for r in card_rank.split(' ')]
    card_dict = {}
    for r_idx, r in enumerate(rank_list):
        card_dict[r] = r_idx

    for a, b in zip(A, B):
        if card_dict[a] > card_dict[b]:
            answer += 1

    return answer


# python 3 program for the above approach
import sys


# Function to check if the current
# string is balanced or not

#Smallest substring with each letter occurring both in uppercase and lowercase
def balanced(small, caps):
    # For every character, check if
    # there exists uppercase as well
    # as lowercase characters
    for i in range(26):
        if (small[i] != 0 and (caps[i] == 0)):
            return 0

        elif ((small[i] == 0) and (caps[i] != 0)):
            return 0
    return 1

def solution2(s):
    import sys
    def balanced(small, caps):

        for i in range(26):
            if (small[i] != 0 and (caps[i] == 0)):
                return 0

            elif ((small[i] == 0) and (caps[i] != 0)):
                return 0
        return 1

    small = [0 for i in range(26)]
    caps = [0 for i in range(26)]
    for i in range(len(s)):
        if (ord(s[i]) >= 65 and ord(s[i]) <= 90):
            caps[ord(s[i]) - 65] += 1
        else:
            small[ord(s[i]) - 97] += 1

    mp = {}
    for i in range(26):
        if (small[i] and caps[i] == 0):
            mp[chr(i + 97)] = 1

        elif (caps[i] and small[i] == 0):
            mp[chr(i + 65)] = 1

    for i in range(len(small)):
        small[i] = 0
        caps[i] = 0

    i = 0
    st = 0

    start = -1
    end = -1

    minm = sys.maxsize

    while (i < len(s)):
        if (s[i] in mp):

            while (st < i):
                if (ord(s[st]) >= 65 and ord(s[st]) <= 90):
                    caps[ord(s[st]) - 65] -= 1
                else:
                    small[ord(s[st]) - 97] -= 1

                st += 1
            i += 1
            st = i
        else:
            if (ord(s[i]) >= 65 and ord(s[i]) <= 90):
                caps[ord(s[i]) - 65] += 1
            else:
                small[ord(s[i]) - 97] += 1

            while (1):
                if (ord(s[st]) >= 65 and ord(s[st]) <= 90 and caps[ord(s[st]) - 65] > 1):
                    caps[ord(s[st]) - 65] -= 1
                    st += 1
                elif (ord(s[st]) >= 97 and ord(s[st]) <= 122 and small[ord(s[st]) - 97] > 1):
                    small[ord(s[st]) - 97] -= 1
                    st += 1
                else:
                    break
            if (balanced(small, caps)):
                if (minm > (i - st + 1)):
                    minm = i - st + 1
                    start = st
                    end = i
            i += 1
    if (start == -1 or end == -1):
        return -1
    else:
        return end +1 -start



def solution3(N):
    if N >= 0:
        str_N = str(N)
        if "5" > str_N[0]:
            return int("5" + str_N)
        for n_idx, n in enumerate(str_N):
            if "5" > n:
                return int(str_N[:n_idx] + "5" + str_N[n_idx:])

        return int(str_N + "5")
    else:
        str_N = str(abs(N))
        if "5" < str_N[0]:
            return int("5" + str_N) * -1
        for n_idx, n in enumerate(str_N):
            if "5" < n:
                return int(str_N[:n_idx] + "5" + str_N[n_idx:]) * -1

        return int(str_N + "5") * -1

def solution3_2(N):
    str_N = str(abs(N))
    answer = int(str_N + "5")

    if N > 0:
        for i in range(len(str_N)):
            answer = max(answer, int(str_N[:i] +"5" + str_N[i:]))
            print(int(str_N[:i] +"5" + str_N[i:]))
    else:
        answer = answer * -1
        for i in range(len(str_N)):
            answer = max(answer, -1 * int(str_N[:i] +"5" + str_N[i:]))
            print(int(str_N[:i] +"5" + str_N[i:]))

    return answer

"""
you are given two passages of text that have been scanned and passed through OCR software. 
(OCR stands for Optical Character Recognition, which is the conversion of printed text into machine-readable strings)

"""


def solution4(S, T):
    def ocr(s):
        t = []
        i = 0
        new_s = ""
        while i < len(s):
            c = s[i]
            # handle digits
            i += 1
            if c.isdigit():
                t.append(c)
                if i == len(s):
                    ocr_len = int(''.join(t))
                    new_s = new_s + ("?" * ocr_len)
            elif len(t) >0:
                ocr_len = int(''.join(t))
                new_s = new_s + ("?" * ocr_len) +c
                t = []
            else:
                new_s +=c

        return new_s
    answer =True
    S_ocr = ocr(S)
    T_ocr = ocr(T)

    if len(S_ocr) == len(T_ocr):
        for sc, tc in zip(S_ocr, T_ocr):
            if sc != tc and sc != "?" and tc != "?":
                return False
        return True
    else:
        return False

print(solution4('A2Le', '2pL1'))

def solution5(S):
    L_pre = [0] * len(S)
    left_idx = 0
    i = 1
    while (i < len(S)):
        if (S[i] == S[left_idx]):
            left_idx = left_idx + 1
            L_pre[i] = left_idx
            i = i + 1
        elif left_idx == 0:
            L_pre[i] = 0
            i = i + 1
        else:
            left_idx = L_pre[left_idx - 1]

    answer = L_pre[len(S) - 1]

    return answer

