class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.permute = []
        visited = set()
        self.backtracking(visited, [], nums)
        return self.permute
        
        
    def backtracking(self,visited,subset,nums):
        if len(subset) == len(nums):
            self.permute.append(subset)
        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                self.backtracking(visited,subset+[nums[i]],nums)
                visited.remove(i)
                
        