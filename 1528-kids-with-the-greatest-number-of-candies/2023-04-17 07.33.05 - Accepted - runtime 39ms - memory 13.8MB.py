class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        new = [i+extraCandies for i in candies]
        oldMax = max(candies)
        output = []
        for i in new:
            output.append(i>=oldMax)
        return output