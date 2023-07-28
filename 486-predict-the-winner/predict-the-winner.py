class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def winner(i: int, j: int) -> int:
            if i == j:
                return nums[i]
            return max(
                nums[i] - winner(i + 1, j),
                nums[j] - winner(i, j - 1),
            )

        return winner(0, len(nums) - 1) >= 0