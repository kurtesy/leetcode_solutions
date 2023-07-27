class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones, reverse = True)
        while len(stones) > 1:
            x,y = stones[0], stones[1]
            print(x,y)
            if x==y:
                stones = stones[2:]
            if x!=y:
                x-=y
                stones[1] = x
                stones = stones[1:]
            stones = sorted(stones, reverse = True)
            print(stones)
        if len(stones) > 0:
            return stones[0]
        return 0
        