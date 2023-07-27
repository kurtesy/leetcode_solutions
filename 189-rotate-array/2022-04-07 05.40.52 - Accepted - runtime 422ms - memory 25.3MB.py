class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        x = k%n
        nums[:] = nums[n-x:]+nums[:n-x]
        