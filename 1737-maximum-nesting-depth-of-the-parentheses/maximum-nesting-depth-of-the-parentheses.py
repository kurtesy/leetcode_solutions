class Solution:
    def maxDepth(self, s: str) -> int:
        curDepth = 0
        maxVal = 0
        if len(s) == 0:
            return 0
        for i in s:
            if i=="(":
                curDepth+=1
                maxVal = max(maxVal, curDepth)
            elif i==")":
                curDepth-=1
        return maxVal