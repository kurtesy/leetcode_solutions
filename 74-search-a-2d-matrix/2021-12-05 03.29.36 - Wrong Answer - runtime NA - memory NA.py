class Solution(object):
    def BS(self, arr, target, left, right):
        if left>right:
            return
        mid = (left+right)//2
        if mid < len(arr) and arr[mid] == target:
            return 'true'
        if mid < len(arr) and arr[mid] > target:
            return self.BS(arr, target, left, mid-1)
        if mid < len(arr) and arr[mid] < target:
            return self.BS(arr, target, mid+1, right)
        return 'false'
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        flatArray = []
        for i in matrix:
            flatArray+=i
        print(flatArray)
        return self.BS(flatArray, target, 0, len(flatArray))
        