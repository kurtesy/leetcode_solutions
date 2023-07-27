class Solution:
    def isHappy(self, n: int) -> bool:
        s = n
        done = []
        while s > 1:
            if s in done:
                return False
            done.append(s)
            s = sum(map(lambda x: int(x)**2, list(str(s))))
        return True
        