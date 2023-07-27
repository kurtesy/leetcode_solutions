class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''.join([i+j for i,j in zip(word1, word2)])
        if len(word1) < len(word2):
            res+=word2[len(word1):]
        else:
            res+=word1[len(word2):]
        return res