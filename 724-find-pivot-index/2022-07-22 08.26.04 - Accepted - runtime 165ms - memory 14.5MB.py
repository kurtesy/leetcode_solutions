class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftSum, rightSum = 0, sum(nums)
        for index, val in enumerate(nums):
            rightSum-=val
            if leftSum == rightSum:
                return index
            leftSum+=val
        return -1
                