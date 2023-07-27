class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        x=[i[0] for i in coordinates]
        y=[i[1] for i in coordinates]
        diff_x1 = x[1]-x[0]
        diff_y1 = y[1]-y[0]
        diff_x2 = x[2]-x[1]
        diff_y2 = y[2]-y[1]
        if diff_x1 != diff_x2:
            return False
        if diff_y1 != diff_y2:
            return False
        for i in range(n-1):
            if x[i+1]-x[i] != diff_x1:
                return False
        for i in range(n-1):
            if y[i+1]-y[i] != diff_y1:
                return False
        return True
        