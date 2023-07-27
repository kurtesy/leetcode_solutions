class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        self.g = image
        def bfs(r,c,m,n):
            print(r,c,m,n)
            if r<0 or r>=m or c<0 or c>=n:
                return
            self.g[r][c] = color
            neighbours = [[0,1], [1,0], [0,-1], [-1,0]]
            for i,j in neighbours:
                if 0<=r+i<m and 0<=c+j<n and self.g[r+i][c+j] != color and self.g[r+i][c+j] != 0:
                    bfs(r+i,c+j,m,n)
            return
        bfs(sr,sc,len(image), len(image[0]))
        return self.g
                    