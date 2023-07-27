class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        Map = {}
        done = []
        for i, j in zip(s,t):
            if j in done and Map[j] != i:
                return False
            if i not in Map:
                Map[i] = j
                Map[j] = i
                done.append(j)
            if i in Map:
                if Map[i] != j:
                    return False
            print(Map)
        return True
        