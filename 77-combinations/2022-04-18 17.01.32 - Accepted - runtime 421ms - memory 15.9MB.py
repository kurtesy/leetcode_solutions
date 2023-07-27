class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.combinations = []
        self.n = n
        self.backtrack(k, [], 1)
        return self.combinations
        
        
    def backtrack(self,k, option, nextIndex):
        if k == 0:
            self.combinations.append(option[:])
        else:
            for i in range(nextIndex, self.n+1):
                option.append(i)
                self.backtrack(k-1, option, i+1)
                option.pop()