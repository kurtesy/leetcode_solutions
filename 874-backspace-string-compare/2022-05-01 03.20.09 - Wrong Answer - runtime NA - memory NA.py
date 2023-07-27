class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        for i in s:
            if i == '#' and len(stack1):
                stack1.pop()
            else:
                stack1.append(i)
        for i in t:
            if i == '#' and len(stack2):
                stack2.pop()
            else:
                stack2.append(i)
        return ''.join(stack2) == ''.join(stack1)