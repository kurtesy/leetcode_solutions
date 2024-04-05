class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in s:
            if len(stack) > 0:
                prev = stack.pop()
                if prev.lower() == i.lower() and ((prev.isupper() and i.islower()) or (i.isupper() and prev.islower())):
                    pass
                else:
                    stack.append(prev)
                    stack.append(i)
            else:
                stack.append(i)
        return ''.join(stack)

