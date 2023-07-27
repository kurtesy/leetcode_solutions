class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        i = 0
        j = 1
        k = 2
        while i<j<k and i<len(nums)-2:
            if nums[i]<nums[k]<nums[j]:
                return True
            if k+1 < len(nums):
                k+=1
                continue
            else:
                if j+1 < len(nums)-1:
                    j+=1
                    k=j+1
                    continue
                else:
                    i+=1
                    j=i+1
                    k=j+1
        return False
                