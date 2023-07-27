class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        d = {k: 0 for k in alpha}
        for a in s:
            d[a]+=1
        count = 0
        nums = [i for i in sorted(d.values(), reverse=True) if i>0]
        
        for i in range(len(nums)):
            while nums[i] in nums[0:i]:
                nums[i] -= 1
                count += 1
                if nums[i] == 0:
                    break
                
        return count
            
        