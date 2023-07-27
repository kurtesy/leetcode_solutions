import math
import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        x = math.ceil(n/2)
        c = collections.Counter(nums)
        ans = -1
        for k,v in c.items():
            if v >= x:
                ans = k
        return ans