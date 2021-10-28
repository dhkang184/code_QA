#https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right, y = 0, len(height) - 1, 0
        ans = 0

        while left < right:

            x = (right - left)

            if height[left] <= height[right]:
                y = height[left]
                left += 1
            else:
                y = height[right]
                right -= 1

            ans = max(x * y, ans)

        return ans