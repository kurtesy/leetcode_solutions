class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(d,visited,ans,nums):
            if len(d)==len(nums):
                ans.append(d.copy())
                return
            
            for i in range(len(nums)):
                if not visited[i]:
                    d.append(nums[i])
                    visited[i] = True
                    backtrack(d,visited,ans,nums)
                    d.pop()
                    visited[i] = False

        visited = [0]*len(nums)
        d,ans = [],[]
        backtrack(d,visited,ans,nums)
        return ans