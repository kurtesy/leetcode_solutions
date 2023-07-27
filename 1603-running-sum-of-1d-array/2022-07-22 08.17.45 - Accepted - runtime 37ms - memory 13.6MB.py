class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sums = []
        last=0
        for i in nums:
            sums.append(last+i)
            last+=i
        return sums