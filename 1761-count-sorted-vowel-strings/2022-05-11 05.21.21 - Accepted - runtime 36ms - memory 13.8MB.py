class Solution:
    def countVowelStrings(self, n: int) -> int:
        n=n+1
        return int(n * (n + 1) * (n + 2) * (n + 3) / 24)