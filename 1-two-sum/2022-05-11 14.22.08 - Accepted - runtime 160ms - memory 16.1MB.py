class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1
        nums = sorted([[val, i] for i, val in enumerate(nums)], key=lambda x:x[0])
        print(nums)
        while right < len(nums) and left <= right:
            if nums[left][0] + nums[right][0] == target:
                return [nums[left][1], nums[right][1]]
            elif nums[left][0] + nums[right][0] > target:
                right-=1
            else:
                left+=1
        
                
        