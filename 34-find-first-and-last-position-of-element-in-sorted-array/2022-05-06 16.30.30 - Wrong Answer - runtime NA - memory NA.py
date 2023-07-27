class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = 0
        ans = [-1, -1]
        while left <= right and right < len(nums):
            if nums[right] == target:
                right+=1
            else:
                if left !=right:
                    ans = [left, right-1]
                right+=1
                left=right
        return ans
                
        