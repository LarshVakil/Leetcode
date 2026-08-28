class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        d =  0 
        x1 , y1 = points.pop()
        while points:
        #better than len(points) != 0 

            x2,y2 = points.pop()
            d+= max(abs(x2-x1) , abs(y2-y1))
            x1 , y1 = x2 , y2

        return d 