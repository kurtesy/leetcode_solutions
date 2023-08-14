import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = heapq.heapify(nums)
        return heapq.nlargest(k, nums)[-1]