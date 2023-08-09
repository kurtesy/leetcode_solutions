class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums = sorted(nums)
        l = len(nums)
        
        def dp(bound):
            arr = [0]*l
            arr[1] = int(nums[1]-nums[0] <= bound)
            for i in range(2, l):
                arr[i] = max(arr[i-2] + int(nums[i]-nums[i-1] <= bound), arr[i-1])
                if arr[i] >= p:
                    return True
            return arr[-1] >= p
        
        le, ri = 0, nums[-1] - nums[0]
        while le < ri:
            mid = (le+ri) // 2
            if dp(mid):
                ri = mid
            else:
                le = mid + 1
        return le