class Solution:
    def paint(self, image, x, y, targetColor, newColor, n, m):
        cur = image[x][y]
        if cur != targetColor:
            return
        image[x][y] = newColor
        directions = [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]
        for i,j in directions:
            if 0<=i<n and 0<=j<m:
                return self.paint(image, i, j, targetColor, newColor, n, m)
            
                
        
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        targetColor = image[sr][sc]
        self.paint(image, sr, sc, targetColor, newColor, len(image), len(image[0]))
        print(image)
        return image
        