class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        counter = 1
        ptr = 0
        while k>0 and ptr < len(arr):
            if arr[ptr] == counter:
                ptr+=1
            else:
                k-=1
            if k==0:
                return counter
            counter+=1
        return arr[ptr-1] + k
