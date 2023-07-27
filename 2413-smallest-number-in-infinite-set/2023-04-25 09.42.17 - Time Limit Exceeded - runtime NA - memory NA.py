from heapq import heapify, heappush, heappop
class SmallestInfiniteSet:

    def __init__(self):
        self.nums = [*range(1,10**6)]
        heapify(self.nums)
        return None

    def popSmallest(self) -> int:
        val = -1
        if len(self.nums)>0:
            val = heappop(self.nums)
        return val

    def addBack(self, num: int) -> None:
        if num not in self.nums:
            heappush(self.nums, num)
        return None
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)