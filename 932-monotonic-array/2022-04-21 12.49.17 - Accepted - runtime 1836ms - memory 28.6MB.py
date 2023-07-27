class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        prev = nums[0]
        inc = False
        dec = False
        for i in nums[1:]:
            if i==prev:
                continue
            if prev < i:
                inc = True
            else:
                dec = True
            if inc and dec:
                return False
            prev = i
        return True
            