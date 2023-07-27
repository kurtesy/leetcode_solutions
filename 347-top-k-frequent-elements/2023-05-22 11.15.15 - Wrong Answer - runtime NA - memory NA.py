class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        ans = []
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

            if freq[i] == k:
                ans.append(i)
        return ans