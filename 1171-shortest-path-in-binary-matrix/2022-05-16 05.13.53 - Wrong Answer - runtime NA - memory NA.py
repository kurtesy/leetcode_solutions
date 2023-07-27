class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        start = [0,0]
        n,m = len(grid), len(grid[0])
        self.steps = 1
        self.end = False
        if grid[start[0]][start[1]] == 1 or grid[n-1][m-1] == 1:
            return -1
        self.dfs(grid, start, n, m)
        print('*'*10)
        return self.steps
        
    def dfs(self, grid, cur, n, m):
        directions = [[1,1],[0,1],[1,0]]
        if cur[0] == n-1 and cur[1] == m-1:
            self.end = True
            return
        for x,y in directions:
            X = cur[0]+x
            Y = cur[1]+y
            if X < n and Y < m and grid[X][Y] == 0:
                if not self.end:
                    self.steps+=1
                print(X,Y, grid[X][Y])
                self.dfs(grid, [X,Y], n, m)
                
                