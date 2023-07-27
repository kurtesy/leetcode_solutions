class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        mem = [-1] * len(questions)
        mem[-1] = questions[-1][0]
        for i in range(len(questions)-2, -1, -1):
            skip = mem[i+1]
            solve = questions[i][0] + (mem[i+1+questions[i][1]] if i+1+questions[i][1] < len(questions) else 0)
            mem[i] = max(mem[i], skip, solve)
        return mem[0]