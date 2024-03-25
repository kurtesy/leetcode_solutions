class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d = set()
        result = []
        for i in nums:
            if i in d:
                result.append(i)
            else:
                d.add(i)
        return result