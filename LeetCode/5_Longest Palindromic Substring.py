#https://leetcode.com/problems/longest-palindromic-substring/

# 20:15~
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def c_check(len, s_list):
            for c_idx, c in enumerate(s_list[:-(len - 1)]):
                c_len = 0
                b_point = True
                while c_len <= len // 2:
                    if s_list[c_idx + c_len] != s_list[c_idx + len -1 -c_len]:
                        b_point = False
                        break
                    c_len += 1

                if b_point:
                    return ''.join(s_list[c_idx: c_idx + len])

        answer= ""
        if len(s) < 2:
            return s
        s_list = list(s)
        m = 0
        l = len(s)
        while m < l:
            mid = (m+l)//2
            mid_c = c_check(mid, s_list)
            if mid_c:
                m = mid +1
                answer = mid_c
            else:
                l = mid -1

        return answer

S = Solution()
print(S.longestPalindrome('babad'))
"""

class Solution:
    def longestPalindrome2(self, s: str) -> str:
        answer = ""
        s_list = list(s)
        if len(s) <=1:
            return s
        l_count = 0
        sub_b_p = True
        l = len(s)
        while l_count <= l // 2:
            if s_list[l_count] != s_list[l - 1 - l_count]:
                sub_b_p = False
                break
            else:
                l_count += 1
        if sub_b_p:
            return ''.join(s_list)

        for l in range(1, len(s)):
            for c_idx, c in enumerate(s_list[:len(s) -l]):
                l_count = 0
                sub_b_p = True
                while l_count <= l//2:
                    if s_list[c_idx + l_count] != s_list[c_idx + l -1 -l_count]:
                        sub_b_p = False
                        break
                    else:
                        l_count += 1
                if sub_b_p:
                    answer = ''.join(s_list[c_idx: c_idx +l])
                    break

        return answer

    def longestPalindrome3(self, s: str) -> str:
        long = ""
        if len(s) <= 1:
            return s

        for i in range(len(s)):
            for j in range(len(s), i, -1):
                if len(long) >= j - i:
                    continue
                elif s[i:j] == s[i:j][::-1]:
                    long = s[i:j]

        return long

    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        i, l = 0, 0
        for j in range(len(s)):
            if s[j - l: j + 1] == s[j - l: j + 1][::-1]:
                i, l = j - l, l + 1
                # print(s[i: i+l])
            elif j - l > 0 and s[j - l - 1: j + 1] == s[j - l - 1: j + 1][::-1]:
                i, l = j - l - 1, l + 2
                # print(s[i: i+l])
        return s[i: i + l]

S = Solution()
print(S.longestPalindrome("accc"))

