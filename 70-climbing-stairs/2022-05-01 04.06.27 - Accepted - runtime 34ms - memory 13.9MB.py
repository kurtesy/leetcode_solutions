class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * 50
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        def climbup(n):
            if dp[n] > -1:
                return dp[n]
            temp = climbup(n-1) + climbup(n-2)
            dp[n] = temp
            return temp
        return climbup(n)
        