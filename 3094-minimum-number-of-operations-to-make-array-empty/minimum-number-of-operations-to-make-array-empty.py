from collections import defaultdict
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for n in nums:
            freq[n]+=1
        result = 0
        for num, cnt in freq.items():
            if cnt == 1:
                return -1
            result += cnt//3
            if cnt%3 != 0:
                result += 1
        return result