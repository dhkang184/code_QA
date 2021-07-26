#https://leetcode.com/problems/reverse-integer/
import math

class Solution:
    def reverse(self, x: int) -> int:
        if math.pow(2,32) <= x or x < -1 * math.pow(2,32):
            return 0

        if x >=0 :
            str_x = str(x)
            ans= int(str_x[::-1])
        else:
            str_x = str(abs(x))
            ans= -1 * (int(str_x[::-1]))

        if -1* math.pow(2,31) <= ans < math.pow(2,31):
            return ans
        else:
            return 0