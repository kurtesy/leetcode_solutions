import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        log_val = math.log(abs(n),4)
        if log_val == int(log_val):
            return True
        return False