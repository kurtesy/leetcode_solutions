class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)
        return None

    def add(self, val: int) -> int:
        inserted = False
        for i in range(len(self.nums)):
            if self.nums[i] >= val:
                self.nums[:] = self.nums[:i]+[val]+self.nums[i:]
                inserted = True
                break
        if not inserted:
            self.nums.append(val)
        # print(self.nums)
        return self.nums[::-1][self.k-1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)