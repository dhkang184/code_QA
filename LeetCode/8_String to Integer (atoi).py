#https://leetcode.com/problems/string-to-integer-atoi/

import math

class Solution:
    def myAtoi(self, s: str) -> int:
        ans = ""
        for c_idx , c in enumerate(s):
            if c == "-" and len(ans) ==0 :
                ans += c
            elif c.isdigit():
                ans +=c
            elif ans =="-" and not c.isdigit():
                ans = ""
            elif len(ans) >0 and not c.isdigit():
                break

        ans = eval(ans)
        if -1 * math.pow(2,31) >= ans:
            return -1 * math.pow(2,31)
        elif math.pow(2, 31) -1 <= ans:
            return math.pow(2, 31) -1
        else:
            return ans

