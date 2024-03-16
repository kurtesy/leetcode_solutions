class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLen = 0
        cnt0 = 0
        cnt1 = 0
        trackingDiff = {0: -1}
        for index,num in enumerate(nums):
            cnt0+=[0,1][num==0]
            cnt1+=[0,1][num==1]
            diff = cnt0-cnt1
            if diff in trackingDiff:
                maxLen = max(maxLen, index-trackingDiff[diff])
            else:
                trackingDiff[diff] = index
        return maxLen
        