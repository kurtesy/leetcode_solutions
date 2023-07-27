class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        pro = 1
        for i in nums:
            pro*=i
        return 1 if pro>0 else -1