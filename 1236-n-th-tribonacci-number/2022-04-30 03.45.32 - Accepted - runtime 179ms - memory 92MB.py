class Solution:
    T = [-1] * 10**7
    T[0] = 0
    T[1] = 1
    T[2] = 1
    def tribonacci(self, n: int) -> int:
        if n <= 2:
            return self.T[n]
        if self.T[n] > -1:
            return self.T[n]
        temp = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        self.T[n] = temp
        return temp
        