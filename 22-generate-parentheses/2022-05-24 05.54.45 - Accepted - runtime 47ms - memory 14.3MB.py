class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        self.res = []
        self.dfs([], 0, 0, n)
        return self.res
        
    def dfs(self, path, l, r, n):
        if 2*n == len(path):
            self.res.append(''.join(path))
            return
        if l < n:
            path+=['(']
            self.dfs(path, l+1, r, n)
            path.pop()
        if r < l:
            path+=[')']
            self.dfs(path, l, r+1, n)
            path.pop()
        