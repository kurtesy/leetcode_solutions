class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * 50
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        def climbup(n):
            if n <= 3:
                return dp[n]
            if dp[n] > -1:
                return dp[n]
            temp = climbup(n-1) + climbup(n-1) - 1
            dp[n] = temp
            return temp
        return climbup(n)
        