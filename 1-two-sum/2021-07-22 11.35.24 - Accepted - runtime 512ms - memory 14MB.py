class Solution(object):
    def twoSum(self, nums, target):
        ans = []
        for i, val in enumerate(nums):
            temp = target - val
            if temp in nums and i != nums.index(temp):
                tempIdx = nums.index(temp)
                ans=[min(tempIdx,i), max(tempIdx,i)]
                break
        return ans
        