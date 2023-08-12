func uniquePathsWithObstacles(obstacleGrid [][]int) int {
    m, n := len(obstacleGrid), len(obstacleGrid[0])
    DP := make([]int, n)
    DP[n - 1] = 1
    for i := m - 1; i >= 0; i-- {
        for j := n - 1; j >= 0; j-- {
            if obstacleGrid[i][j] == 1 {
                DP[j] = 0
            } else if j + 1 < n {
                DP[j] = DP[j] + DP[j + 1]
            }
        }
    }
    return DP[0]
}