class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        p = arr[1]
        diff = p - arr[0]
        for i in arr[2:]:
            if i-p != diff:
                return False
            p = i    
        return True

