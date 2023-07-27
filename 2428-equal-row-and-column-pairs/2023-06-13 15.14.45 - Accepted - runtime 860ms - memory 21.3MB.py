class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cnt = 0
        trans = list(zip(*grid))
        for row in grid:
            for col in trans:
                if row == list(col):
                    cnt+=1
        return cnt