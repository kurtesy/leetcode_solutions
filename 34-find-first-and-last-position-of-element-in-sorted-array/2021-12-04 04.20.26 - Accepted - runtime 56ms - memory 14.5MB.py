class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = -1
        last = -1
        for i, val in enumerate(nums):
            if val == target and first < 0:
                first = i
            if val == target:
                last = i
        return [first, last]