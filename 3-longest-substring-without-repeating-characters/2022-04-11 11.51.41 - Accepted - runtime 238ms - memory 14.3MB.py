class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        right = 0
        res = 0
        if len(s) == 1:
            return 1
        while left <= right:
            window = s[left:right+1]
            right+=1
            if right >= len(s):
                break
            search = window.find(s[right])
            if search > -1:
                print(window, search, s[right], left, right)
                res = max(res, len(window))
                left += search + 1
        res = max(res, len(window))
        print(res)
        return res
        
        