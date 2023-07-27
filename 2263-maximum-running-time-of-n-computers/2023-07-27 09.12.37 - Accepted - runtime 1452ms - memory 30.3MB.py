class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def possible(batteries,minute,n):
            computer = 0 
            i = len(batteries)-1 
            while batteries[i]>=minute and i>=0:
                computer+=1 
                i-=1 
            if computer+((sum(batteries[:i+1]))//minute)>=n: 
                return True
            return False
        batteries.sort() 
        low  = batteries[0]
        high= int(1e32)
        ans = 1 
        while low<=high:
            minute = low+(high-low)//2 
            if possible(batteries,minute,n): 
                ans = minute 
                low=minute+1 
            else:
                high=minute-1 
        return ans 