class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0
        found = False
        while i<len(haystack) and j <len(needle):
            if haystack[i] == needle[j]:
                i+=1
                j+=1
                found = True
            else:
                found = False
                j = 0
                i+=1
        print(j,found)
        if found:
            return i-2
        return -1