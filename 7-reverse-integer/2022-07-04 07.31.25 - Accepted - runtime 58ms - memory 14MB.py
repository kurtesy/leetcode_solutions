class Solution:
    def reverse(self, x: int) -> int:
        limit = 2**31
        temp = str(x)[::-1]
        if temp[-1] == '-':
            revI = -1*int(temp[:-1])
        else:
            revI = int(temp)
        if -limit<=revI<limit:
            return revI
        return 0