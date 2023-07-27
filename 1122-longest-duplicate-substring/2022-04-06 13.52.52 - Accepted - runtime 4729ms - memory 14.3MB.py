class Solution:
    def longestDupSubstring(self, s: str) -> str:
        j=1
        ans = ''
        for i in range(0,len(s)):
            window = s[i:i+j]
            remaining = s[i+1:]
            while window in remaining:
                ans = window
                j += 1
                window = s[i:i+j]
        print(ans)
        return ans
            
        