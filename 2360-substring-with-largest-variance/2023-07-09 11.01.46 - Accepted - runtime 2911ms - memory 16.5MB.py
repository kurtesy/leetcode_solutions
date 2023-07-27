class Solution:
    def largestVariance(self, s: str) -> int:
        res = 0
        freq = Counter(s)
        for a in freq.keys():
            for b in freq.keys():
                if a == b:
                    continue
                a_count = b_count = 0
                a_left = freq[a]
                for c in s:
                    if c == a or c == b:
                        if c == a:
                            a_count += 1
                            a_left -= 1
                        elif c == b:
                            b_count += 1
                        if b_count < a_count and a_left > 0:
                            a_count = b_count = 0
                        if a_count > 0 < b_count:
                            res = max(res, b_count - a_count)
        return res