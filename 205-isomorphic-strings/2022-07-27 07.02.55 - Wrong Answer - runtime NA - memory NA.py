class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        Map = {}
        for i, j in zip(s,t):
            if i not in Map:
                Map[i] = j
            else:
                if Map[i] != j:
                    return False
        return True
        