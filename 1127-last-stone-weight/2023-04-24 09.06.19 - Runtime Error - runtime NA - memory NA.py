class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones)
        while len(stones) > 1:
            slast = stones[-2]
            last = stones[-1]
            diff = last-slast
            stones = stones[:-2]
            if diff > 0:
                stones.append(diff)
                stones = sorted(stones)
            print(stones)
        return stones[0]


