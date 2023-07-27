class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff = high-low
        cnt = (diff//2)+(1 if high%2!=0 or low%2!=0 else 0)
        return cnt