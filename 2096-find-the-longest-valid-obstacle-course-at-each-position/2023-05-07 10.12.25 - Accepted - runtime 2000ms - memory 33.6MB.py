class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        stack = [] 
        ans = []
        
        for o in obstacles: 
            if not stack or o >= stack[-1]:
                stack.append(o) 
                ans.append(len(stack)) 
            else:
                left, right = 0, len(stack) - 1
                while left <= right:
                    mid = left + (right - left) // 2
                    if stack[mid] <= o:
                        left = mid + 1
                    else:
                        right = mid - 1
                stack[left] = o
                ans.append(left + 1)
        
        return ans