class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        sPoints = sorted(points, key=lambda x:x[0])
        print(sPoints)
        unique = 1
        end = sPoints[0][1]
        
        for balloon in sPoints[1:]:
            if balloon[0] > end: 
                unique += 1  
                end = balloon[1] 
            else:
                end = min(end, balloon[1])
        
        return unique

        