class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        def abs(a , b):
            o = a - b
            if o < 0 :
                o = -o
            return o
        l = len(s)
        
        for i in range(l-1):
            sum += abs(ord(s[i]) , ord(s[i+1]))
        return sum
