class Solution:
    def mirrorDistance(self, n: int) -> int:
        m = str(n)
        rev = [0] * len(m)

        for i in range(len(m)):
            rev[i] = m[len(m)- 1 - i]
        
        reverse = ''.join(rev)
        out = (int(reverse) - n)

        if out < 0 :
            out = -out 
        
        return out 