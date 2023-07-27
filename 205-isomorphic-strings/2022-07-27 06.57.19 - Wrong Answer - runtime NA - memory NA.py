class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        freqS = {}
        freqT = {}
        for i in s:
            if i in freqS:
                freqS[i]+=1
            else:
                freqS[i]=1
        for i in t:
            if i in freqT:
                freqT[i]+=1
            else:
                freqT[i]=1
        for i,j in zip(sorted(freqS.values()), sorted(freqT.values())):
            if i != j:
                return False
        return True
        