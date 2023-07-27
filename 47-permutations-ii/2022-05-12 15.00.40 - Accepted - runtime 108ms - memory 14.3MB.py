class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        nums.sort()
        self.dfs(nums, [])
        return self.ans
    
    def dfs(self, nums, path):
        if not nums:
            self.ans.append(path)
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[0:i]+nums[i+1:], path+[nums[i]])
        