class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freq = {}
        ans = 0
        for i in chars:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        for w in words:
            nono = False
            for c in w:
                if not (c in freq and freq[c] >= w.count(c)):
                    nono = True
            if not nono:
                ans += len(w)
        return ans
        