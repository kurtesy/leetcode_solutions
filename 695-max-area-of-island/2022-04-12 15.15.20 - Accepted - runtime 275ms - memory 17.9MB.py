class Solution:
    def area(self, grid, n,m,x,y):
        directions = [[x+1,y], [x-1,y], [x,y+1], [x,y-1]]
        if x>=n or y>=m or x<0 or y<0 or grid[x][y] == 0:
            return 0
        grid[x][y] =0
        s = 0
        for i,j in directions:
            s+=self.area(grid,n,m,i,j)
        return s+1
            
                
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count = max(self.area(grid, n,m,i,j), count)
                    print(count)
        return count