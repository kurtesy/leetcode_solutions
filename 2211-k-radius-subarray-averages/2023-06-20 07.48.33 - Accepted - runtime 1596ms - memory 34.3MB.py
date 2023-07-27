class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # Get the length of the nums list
        n = len(nums)
        
        # Handle edge cases
        if n == 1:
            if k < n:
                return nums
            return [-1]
        
        if k > n:
            return [-1] * n
        
        # Initialize prefix sum array
        psum = [0] * n
        psum[0] = nums[0]
        
        # Calculate the prefix sum
        for i in range(1, n):
            psum[i] = psum[i - 1] + nums[i]
        
        # Define the lower and upper limits for calculating averages
        L = k
        H = n - k
        
        # Initialize the answer array with -1
        ans = [-1] * n
        
        # Calculate the range of values for averaging
        r = 2 * k + 1
        
        # If the range is larger than the total number of elements, return the answer array
        if r > n:
            return ans
        
        # Calculate the average for the first element
        ans[L] = psum[L + k] // r
        
        c = 0
        # Calculate the averages for the remaining elements
        for i in range(L + 1, H):
            ans[i] = (psum[i + k] - psum[c]) // r
            c += 1
        
        return ans