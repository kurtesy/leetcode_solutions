class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        x = 0
        k = 0
        for i in range(n):
            x+=mat[i][i] + mat[i][n-i-1]
            k+=1
        if n%2==1:
            x = x - mat[n//2][n//2]
        return x