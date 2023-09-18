class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldier_freq = {}
        result = []
        for index,row in enumerate(mat):
            soldier_cnt = row.count(1)
            soldier_freq[index] = soldier_cnt
        for index, cnt in sorted(soldier_freq.items(), key=lambda x: (x[1],x[0])):
            k-=1
            result.append(index)
            if k<=0:
                break
        return result