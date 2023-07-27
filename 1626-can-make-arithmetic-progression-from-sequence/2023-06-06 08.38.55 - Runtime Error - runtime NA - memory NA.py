class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        res = []
        max_num = max(arr)
        for i in arr:
            if max_num-i>0:
                res.append(max_num-i)
        res.sort()
        ref = res[0]
        for i in res:
            if i%ref != 0:
                return False
        return True

