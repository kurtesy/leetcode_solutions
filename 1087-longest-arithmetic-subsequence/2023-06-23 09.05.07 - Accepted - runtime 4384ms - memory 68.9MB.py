class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}; res = 2
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                diff = nums[j] - nums[i]
                dp[j, diff] = dp.get((i, diff), 1) + 1
                res = max(res, dp[(j, diff)])
        return res