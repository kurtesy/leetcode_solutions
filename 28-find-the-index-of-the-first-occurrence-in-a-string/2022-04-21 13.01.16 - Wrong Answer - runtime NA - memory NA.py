class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0
        found = False
        ans = -1
        while i<len(haystack) and j <len(needle):
            if haystack[i] == needle[j]:
                i+=1
                j+=1
                if not found:
                    ans = i
                found = True
            else:
                found = False
                j = 0
                i+=1
        if found:
            return ans-1
        return -1