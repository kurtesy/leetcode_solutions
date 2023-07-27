class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        rods.sort()
        b = 0
        ra = list(accumulate(rods))
        @lru_cache(None)
        def r(ma, mi, i):
            nonlocal b
            nonlocal ra
            if ma == mi:
                b = max(b, ma)
            if i == -1:
                return 0
            if mi + ma + ra[i] <= b + b:
                return 0
            if mi + ra[i] == ma:
                b = max(ma, b)
                return 0
            if mi + ra[i] < ma:
                return 0
            

            r(ma, mi, i - 1)
            r(max(ma, mi + rods[i]), min(ma, mi + rods[i]), i - 1)
            r(ma + rods[i], mi, i - 1)
            return 0
        r(0,0, len(rods) - 1)
        return b
