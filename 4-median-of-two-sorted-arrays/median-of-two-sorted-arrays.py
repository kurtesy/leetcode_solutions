class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p1 = 0
        p2 = 0
        merged = []
        while p1 < len(nums1) and p2 < len(nums2):
            num1 = nums1[p1]
            num2 = nums2[p2]
            if num1 < num2:
                merged.append(num1)
                p1+=1
            else:
                merged.append(num2)
                p2+=1
        while p1 < len(nums1):
            merged.append(nums1[p1])
            p1+=1
        while p2 < len(nums2):
            merged.append(nums2[p2])
            p2+=1
        n = len(merged)
        mid = n//2
        if n%2 == 0:
            return (merged[mid-1]+merged[mid])/2
        else:
            return merged[mid]