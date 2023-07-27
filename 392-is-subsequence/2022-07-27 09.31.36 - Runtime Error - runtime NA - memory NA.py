class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s=list(s)
        if len(s) == 0:
            return True
        for i in t:
            if i == s[0]:
                s.pop(0)
        return len(s) == 0