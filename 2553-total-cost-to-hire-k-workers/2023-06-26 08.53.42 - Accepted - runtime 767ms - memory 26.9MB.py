import heapq as hq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        leftIdx, rightIdx = candidates, max(len(costs)-candidates, candidates)-1
        leftHeap, rightHeap = costs[:leftIdx], costs[rightIdx+1:]
        hq.heapify(leftHeap)
        hq.heapify(rightHeap)
        cost = 0
        for i in range(k):
            if leftHeap and rightHeap:
                if leftHeap[0]<=rightHeap[0]:
                    if leftIdx <= rightIdx:
                        cost += hq.heapreplace(leftHeap, costs[leftIdx])
                        leftIdx += 1
                    else: cost += hq.heappop(leftHeap)
                else:
                    if leftIdx <= rightIdx:
                        cost += hq.heapreplace(rightHeap, costs[rightIdx])
                        rightIdx -= 1
                    else: cost += hq.heappop(rightHeap)
            elif leftHeap: cost += hq.heappop(leftHeap)
            else: cost += hq.heappop(rightHeap)
        return cost