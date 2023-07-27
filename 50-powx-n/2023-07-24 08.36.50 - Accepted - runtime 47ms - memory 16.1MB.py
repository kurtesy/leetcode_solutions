class Solution:
    def myPow(self, x: float, n: int) -> float:
        def mul(x,n):
            res = 1
            while n > 0:
                lastBit = n&1
                if lastBit:
                    res *= x
                x *= x
                n = n >> 1
            return res
        res = mul(x,abs(n))
        if n < 0:
            res = 1/res
        return res

            