class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans = -1
        for i, val in enumerate(nums):
            if val == target:
                ans = i
        return ans