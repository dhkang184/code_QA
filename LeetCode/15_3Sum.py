class Solution:
    def threeSum1(self, nums):
        from itertools import combinations
        if len(nums) <3:
            return []
        nums = sorted(nums)
        c_list = list(combinations(nums,3))
        answer =[]

        for c in c_list:
            if sum(c) == 0:
                answer.append(c)
        answer = list(set(answer))
        return [list(a) for a in answer ]

    def threeSum2(self, nums):

        if len(nums) <3:
            return []
        nums = sorted((nums))
        answer = []

        for n1 in range(len(nums)-2):
            if nums[n1] + nums[-2] + nums[-1] <0 or nums[n1] + nums[n1+1] +nums[n1+2] >0:
                continue
            for n2 in range(n1+1, len(nums)-1):
                if nums[n1] + nums[n2] + nums[-1] <0 or nums[n1] + nums[n2] + nums[n2+1] >0:
                    continue
                for n3 in range(n2+1,len(nums)):
                    sum_n = nums[n1]+nums[n2] +nums[n3]
                    if sum_n == 0:
                        answer.append((nums[n1], nums[n2], nums[n3]))
                    if sum_n >0:
                        break
        return [list(a) for a in list(set(answer))]

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <3:
            return []
        nums = sorted((nums))
        answer = []
        for left in range(len(nums)-2):
            if 0<left and nums[left] == nums[left-1]:
                continue

            mid = left+1
            end = len(nums)-1
            while end> mid:
                sums = nums[left] + nums[mid] + nums[end]
                if sums >=0:
                    if sums ==0:
                        answer.append([nums[left], nums[mid], nums[end]])
                    end -= 1
                    while nums[end] == nums[end + 1] and end> mid:
                        end -= 1
                elif sums <0:
                    mid +=1
                    while nums[mid] == nums[mid -1] and end> mid:
                        mid +=1
        return answer



S= Solution()
S.threeSum([-1,0,1,2,-1,-4])






