class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 1
        curSum = nums[left]+nums[right]
        minLen = 10**9
        while left <= right and right < len(nums):
            if curSum == target:
                minLen = min(right-left, minLen)
                left += 1
                right = left+1
                curSum = nums[left]
            if curSum > target:
                left += 1
                right = left
                curSum = nums[left]
            else:
                right+=1
                if right > len(nums) - 1:
                    break
                curSum+=nums[right]
        print(minLen, curSum)
        return minLen