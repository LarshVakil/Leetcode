class Solution:
    def maxDistinct(self, s: str) -> int:
        unique = { }
        for char in s:
            if char in unique:
                unique[char] += 1 

            else :
                unique[char] = 1 
        return len(unique)