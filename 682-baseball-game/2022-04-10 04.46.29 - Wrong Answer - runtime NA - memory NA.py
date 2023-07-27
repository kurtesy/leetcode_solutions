class Stack:
    def __init__(self):
        self.stack = []
    def add(self, val):
        self.stack.append(val)
    def pop(self):
        return self.stack.pop()
    def seek(self, posFromLast):
        n = len(self.stack)
        return self.stack[n-posFromLast-1]
    def sumAll(self):
        return sum(self.stack)
    

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = Stack()
        for op in ops:
            if op == 'C':
                stack.pop()
            elif op == 'D':
                last = stack.pop() * 2
                stack.add(last)
            elif op == '+':
                second = stack.seek(0)
                first = stack.seek(1)
                stack.add(first+second)
            else:
                stack.add(int(op))
        return stack.sumAll()
            
                