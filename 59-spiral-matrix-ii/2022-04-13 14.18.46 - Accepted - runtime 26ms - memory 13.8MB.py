class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        grid = [[0]*n for i in range(n)]
        r = 0
        c = 0
        dr=1
        dc=0
        for i in range(n*n):
            grid[c][r] = i + 1
            if not 0 <= r + dr < n or not 0 <= c + dc < n or grid[c+dc][r+dr] != 0:
                dr, dc = -dc, dr
            r, c = r + dr, c + dc
        return grid
            