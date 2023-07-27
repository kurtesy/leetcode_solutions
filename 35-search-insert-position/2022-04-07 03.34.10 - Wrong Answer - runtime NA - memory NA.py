class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = (left+right)//2
            if mid > len(nums):
                return -1
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid-1
            elif target > nums[mid]:
                left = mid+1
        return right