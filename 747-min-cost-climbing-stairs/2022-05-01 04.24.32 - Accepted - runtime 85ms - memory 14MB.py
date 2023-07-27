class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        dp = [0] * (N + 2)                           
        for i in range(N - 1, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2]) 
        return min(dp[0], dp[1])    
        