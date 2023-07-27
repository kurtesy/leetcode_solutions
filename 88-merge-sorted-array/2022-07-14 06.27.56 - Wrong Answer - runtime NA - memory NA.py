class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        print(nums1, nums2)
        i = 0
        j = 0
        while i<m+n and j<n:
            print(i, nums1[i], j)
            if nums1[i] == 0:
                nums1[i] = nums2[j]
                i+=1
                j+=1
            elif nums1[i] < nums2[j]:
                i+=1
            else:
                nums1.insert(i,nums2[j])
                nums1.pop()
                i+=1
                j+=1
        print(nums1)
        