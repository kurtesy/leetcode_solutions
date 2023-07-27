class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_alt = 0
        res = [current_alt, gain[0]]
        for i in range(1, len(gain)):
            res.append(res[i]+gain[i])
        return max(res)