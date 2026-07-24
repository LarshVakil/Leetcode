class Solution:
    def maxArea(self, height: List[int]) -> int:
        left , right = 0 , len(height) - 1
        max_a = 0

        while left < right:
            area = min(height[left] , height[right])*(right - left)
            if area > max_a:
                max_a = area 
            if height[left] < height[right]:
                left+= 1 
            else:
                right -= 1
            
        return max_a

        
        return max_a
