class Solution:
    fibs = [-1] * 10**7
    fibs[0] = 0
    fibs[1] = 1
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        if self.fibs[n] > -1:
            return self.fibs[n]
        temp = self.fib(n-1) + self.fib(n-2)
        self.fibs[n] = temp
        return temp