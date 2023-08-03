class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lookup = {'2': 'abc','3': 'def','4': 'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        combinations = ['']
        charset = []
        for digit in digits:
            charset.append(lookup[digit])
        for i in range(len(charset)):
            combinations = [c+charset[i][j] for c in combinations for j in range(len(charset[i]))]
        
        return [] if combinations[0] == '' else combinations