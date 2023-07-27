class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        m=len(matrix[0])
        firstRowZero = False
        firstColZero = False
        for i in matrix[0]:
            if i == 0:
                firstRowZero = True
                break
        for i in zip(*matrix)[0]:
            if i == 0:
                firstColZero = True
                break
        
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if firstRowZero:
            for j in range(m):
                matrix[0][j] = 0
        if firstColZero:
            for i in range(n):
                matrix[i][0] = 0
        return matrix
                