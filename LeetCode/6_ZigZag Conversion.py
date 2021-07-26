#https://leetcode.com/problems/zigzag-conversion/
# 21:40~

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans_list = [[] for _ in range(numRows)]
        if numRows ==1:
            return s
        for c_idx, c in enumerate(s):
            list_idx = c_idx % (2*numRows -2)
            if list_idx >= numRows:
                list_idx = numRows-2 - (list_idx - numRows)
            ans_list[list_idx].append(c)

        ans = ""
        for ans_ in ans_list:
            ans += ''.join(ans_)

        return ans


S = Solution()
S_c = S.convert(s = 'PAYPALISHIRING', numRows=3)