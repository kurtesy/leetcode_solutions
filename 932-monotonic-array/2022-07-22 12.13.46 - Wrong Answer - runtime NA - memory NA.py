class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return True
        trend = 1 if nums[0] < nums[1] else -1
        for i in range(1, len(nums)-1):
            if nums[i] > nums[i+1] and trend == 1:
                return False
            if nums[i] < nums[i+1] and trend == -1:
                return False
        return True