class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [('$', 0)]
        for c in s:
            if stack[-1][0] == c:
                stack[-1] = (c, stack[-1][1]+1)
            else:
                stack.append((c, 1))
            if stack[-1][1] == k:
                stack.pop()
        return ''.join([x*y for x,y in stack])
            
        