from collections import OrderedDict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = OrderedDict()
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        # print(freq)
        for k,v in freq.items():
            if v == 1:
                return s.index(k)
        return -1
        