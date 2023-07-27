class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        for s,e in sorted(intervals, key=lambda x: x[0]):
            if res and s <= res[-1][1]:
                res[-1][1]=e
            else:
                res+=[[s,e]]
        return res