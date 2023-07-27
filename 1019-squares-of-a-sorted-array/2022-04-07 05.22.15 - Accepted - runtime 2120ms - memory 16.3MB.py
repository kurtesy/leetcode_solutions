class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        result = []
        while left <= right:
            x,y = abs(nums[left]), abs(nums[right])
            if x < y:
                result = [y**2] + result
                right-=1
            if x >= y:
                result = [x**2] + result
                left+=1
        return result
                
                
            
            
            
        