class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == None or needle == None:
            return -1
        i, j, m, n = -1, 0, len(haystack), len(needle)
        next = [-1] * n
        while j < n - 1:  
            if i == -1 or needle[i] == needle[j]:   
                i, j = i + 1, j + 1
                next[j] = i
            else:
                i = next[i]
        i = j = 0
        while i < m and j < n:
            if j == -1 or haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            else:
                j = next[j]
        if j == n:
            return i - j
        return -1