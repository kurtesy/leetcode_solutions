class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        d= {}
        cnt=0
        for w in words:
            if w[0] in d:
                d[w[0]].append(w)
            else:
                d[w[0]] = [w]
        for ch in s:
            if ch in d:
                wList = d[ch]
            else:
                wList = []
            d[ch] = []
            for w in wList:
                if len(w) == 1:
                    cnt+=1
                else:
                    if w[1] in d:
                        d[w[1]].append(w[1:])
                    else:
                        d[w[1]] = [w[1:]]
        return cnt