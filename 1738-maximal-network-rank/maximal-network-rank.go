
func maximalNetworkRank(n int, roads [][]int) int {
	graph := make([][]bool, n)
	for i := 0; i < n; i++ {
		graph[i] = make([]bool, n)
	}
	degree := make([]int, n)

	for _, road := range roads {
		graph[road[0]][road[1]] = true
		graph[road[1]][road[0]] = true
		degree[road[0]]++
		degree[road[1]]++
	}
	var maxConnection int
	for i := 0; i < n; i++ {
		for j := i+1; j < n; j++ {
			if graph[i][j] {
				maxConnection = max(maxConnection, degree[i]+degree[j]-1)
			} else {
				maxConnection = max(maxConnection, degree[i]+degree[j])
			}
		}
	}
	return maxConnection
}
func max(x, y int) int {
	if x >= y {
		return x
	}
	return y
}