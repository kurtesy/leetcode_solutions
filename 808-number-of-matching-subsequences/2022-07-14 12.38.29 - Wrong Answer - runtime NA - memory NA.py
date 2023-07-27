class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ref = {chr(k): 0 for k in range(97, 98+26)}
        cnt = 0
        for ch in s:
            ref[ch]+=1
        for w in words:
            alpha = {chr(k): 0 for k in range(97, 98+26)}
            for ch in w:
                alpha[ch]+=1
            isSub = True
            for k, v in alpha.items():
                if v>0 and ref[k]-v < 0:
                    isSub = False
            cnt+=1 if isSub else 0
        return cnt
                    
            
        
        