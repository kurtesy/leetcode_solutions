class Solution:
    def longestPalindrome(self, s: str) -> str:
        curMax = 0
        ans = ''
        for i in range(len(s)):
            subStr = self.build(s, i, i)
            if curMax < len(subStr):
                curMax = len(subStr)
                ans = subStr
            subStr = self.build(s, i, i+1)
            if curMax < len(subStr):
                curMax = len(subStr)
                ans = subStr
        return ans
    def build(self, s, l, r):
        while l>-1 and r<len(s) and s[l] == s[r]:
            l-=1
            r+=1
        return s[l+1:r]
            