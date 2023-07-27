class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        """
            num1 = 1,3,5,7 | 
            num2 = 5,1,7,3
        """
        m, n = len(nums1), len(nums2)
        if m < n:
            nums1, nums2, m, n = nums2, nums1, n, m
        mem = [0] * (n + 1)
        for i in range(1, m + 1):
            prev = 0
            for j in range(1, n + 1):
                curr = mem[j]
                if nums1[i-1] == nums2[j-1]:
                    mem[j] = prev + 1
                else:
                    mem[j] = max(mem[j-1], curr)
                prev = curr
        return mem[n]