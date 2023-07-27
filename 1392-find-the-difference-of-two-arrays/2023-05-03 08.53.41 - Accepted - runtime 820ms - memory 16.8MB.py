class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        alle = nums1+nums2
        first = []
        second = []
        for i in set(alle):
            if i not in nums2:
                first.append(i)
            if i not in nums1:
                second.append(i)
        return [first, second]