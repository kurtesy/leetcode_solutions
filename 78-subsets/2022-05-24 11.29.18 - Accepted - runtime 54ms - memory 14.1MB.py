class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.subs(nums, [])
        return self.res
    def subs(self, nums, path):
        self.res.append(path)
        for i in range(len(nums)):
            self.subs(nums[i+1:], path+[nums[i]])
        