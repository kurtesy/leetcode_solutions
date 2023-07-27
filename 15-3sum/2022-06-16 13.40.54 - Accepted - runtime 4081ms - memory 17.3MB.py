class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        print(nums)
        res = set()
        target = 0
        i = 0
        while i < n:
            first = nums[i]
            left = i+1
            right = n-1
            while left < right:
                if first + nums[left] + nums[right] == target:
                    res.add((first, nums[left],nums[right]))
                    left+=1
                    right-=1
                elif first + nums[left] + nums[right] < target:
                    left+=1
                else:
                    right-=1
            i+=1
        return res

        
                
            