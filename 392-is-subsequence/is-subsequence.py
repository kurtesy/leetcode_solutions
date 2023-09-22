class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr = 0
        s = list(s)
        while len(s)>0 and ptr < len(t):
            char = t[ptr]
            if char == s[0]:
                s.pop(0)
            ptr+=1
            print(s)
        return len(s) == 0
        
        