class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        i = 0
        j = 1
        k = 2
        s = set(nums)
        if len(s)<=2:
            return False
        prev = nums[0]
        temp = []
        for i in nums[1:]:
            if prev != i:
                temp.append(prev)
            prev = i
        nums = temp[:]
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
                