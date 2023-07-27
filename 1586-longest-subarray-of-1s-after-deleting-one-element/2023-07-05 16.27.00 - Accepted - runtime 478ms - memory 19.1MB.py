class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest=0
        i=0
        j=0
        dic={1:0, 0:0}
        while(j<len(nums)):
            dic[nums[j]]+=1
            if dic[0]>1:
                dic[nums[i]]-=1
                i+=1
            longest=max(longest,j-i)
            j+=1  
        return longest