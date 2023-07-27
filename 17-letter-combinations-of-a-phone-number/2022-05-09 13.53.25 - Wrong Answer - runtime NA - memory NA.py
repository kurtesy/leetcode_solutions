class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.ans = []
        self.d = {1: 'abc', 2: 'def', 3: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        self.combinations(digits, 0, '')
        return self.ans
        
    def combinations(self, digits, i, sub):
        if i == len(digits):
            self.ans.append(sub)
            return
        for c in self.d[int(digits[i])-1]:
            sub+=c
            self.combinations(digits, i+1, sub)
            sub = sub[:-1]
        
        
        