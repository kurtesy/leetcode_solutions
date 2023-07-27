class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        ans = []
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        ans = sorted(freq.items(), key=lambda x:x[1], reverse=True)[:k]
        return [i[0] for i in ans]