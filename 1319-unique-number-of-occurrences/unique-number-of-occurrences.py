from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        frequency = Counter(arr)
        done = []
        for count in frequency.values():
            if count not in done:
                done.append(count)
            else:
                return False
        return True

        