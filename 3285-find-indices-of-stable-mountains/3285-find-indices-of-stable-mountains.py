class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        ans = []
        height.pop()
        for i in range(len(height)):
            if height[i] > threshold:
                ans.append(i+1)
        
        return ans
            