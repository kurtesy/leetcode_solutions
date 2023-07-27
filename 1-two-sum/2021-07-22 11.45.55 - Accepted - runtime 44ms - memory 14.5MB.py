class Solution(object):
    def twoSum(self, nums, target):
        ans = []
        diffRef = {}
        for i, val in enumerate(nums):
            diffRef[target-val] = i
        for i, val in enumerate(nums):
            if val in diffRef and diffRef[val] != i:
                ans = [min(diffRef[val], i), max(diffRef[val], i)]
                break
        return ans
        