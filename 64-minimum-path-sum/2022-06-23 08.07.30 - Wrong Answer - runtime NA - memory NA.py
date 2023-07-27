class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        start = [0,0]
        minSum = 10**9
        n,m=len(grid), len(grid[0])
        def bfs(cur, nextDir, curSum):
            nonlocal minSum
            nextCell = [cur[0]+nextDir[0], cur[1]+nextDir[1]]
            # print(nextCell,n,m)
            if nextCell[0] >= n or nextCell[1] >= m:
                return
            curSum += grid[nextCell[0]][nextCell[1]]
            if nextCell[0] == n-1 and nextCell[1] == m-1:
                minSum=min(minSum, curSum)
                return
            for d in [[0,1],[1,0]]:
                bfs(nextCell, d, curSum)
            
        bfs(start, [1,0], grid[0][0])
        bfs(start, [0,1], grid[0][0])
        print(minSum)
        return minSum
            
        