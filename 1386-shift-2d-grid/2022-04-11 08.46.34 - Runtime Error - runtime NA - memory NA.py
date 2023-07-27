class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n = len(grid), len (grid[0])
        newGrid = [[-1] * m for i in range(n)]
        for i in range(k):
            for x in range(m):
                for y in range(n):
                    if y == n-1 and x==m-1:
                        newGrid[0][0] = grid[x][y]
                    elif y == n-1:
                        newGrid[x+1][0] = grid[x][y]
                    else:
                        newGrid[x][y+1] = grid[x][y]
            grid = [row[:] for row in newGrid]
            print(grid)
        if k == 0:
            return grid
        print(newGrid)
        return newGrid