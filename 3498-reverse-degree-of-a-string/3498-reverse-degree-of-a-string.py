class Solution:
    def reverseDegree(self, s: str) -> int:
        c = 0 
        for i in range(len(s)):
            x = 26 - (ord(s[i]) - 97 )
            y = x * (i+1)

            c += y 
        
        return c 

            