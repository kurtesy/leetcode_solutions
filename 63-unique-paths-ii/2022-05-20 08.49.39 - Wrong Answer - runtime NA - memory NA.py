class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.count = 0
        self.dfs(obstacleGrid, '', 0, 0)
        return self.count
        
    def dfs(self, grid, path, i, j):
        print(path, i,j)
        if i == len(grid)-1 and j == len(grid[0])-1:
            self.count+=1
            return
        # left or down
        for x,y in [[0,1], [1,0]]:
            if i+x < len(grid) and j+y < len(grid[0]) and grid[i+x][j+y] == 0:
                self.dfs(grid, path+f'({i+x}, {j+y})', i+x,j+y)
            if i+x < len(grid) and j+y >= len(grid[0]) and grid[i+x][j] == 0 and x>0:
                self.dfs(grid, path+f'({i+x}, {j})', i+x,j)
            elif i+x >= len(grid) and j+y < len(grid[0]) and grid[i][j+y] == 0 and y>0:
                self.dfs(grid, path+f'({i}, {j+y})', i,j+y)
            
        