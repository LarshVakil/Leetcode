class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        n = len(points) 

        if n <= 2:
            return n
        
        ans = 1
        for i in range(n):
            slopes = {}
            x1 , y1 = points[i]

            for j in range (i+1 , n):
                x2 , y2 = points[j]

                dx = x2 - x1  
                dy = y2 - y1

                g = math.gcd(dx,dy)
                #to get exact for hashmap
                slope = (dx//g,dy//g) if dx > 0 or (dx ==0 and dy > 0) else (-dx//g , -dy//g)

                if slope in slopes:
                    slopes[slope] += 1
                else:
                    slopes[slope] = 1

                total_points = slopes[slope]  + 1

                if total_points > ans:
                    ans = total_points 

        return ans