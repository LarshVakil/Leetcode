class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        s1  = 0
        s2 =0
        arr = [int(x) for x in str(n)]
        for i in arr:
            s1 += i
            s2 += i*i
        if s2-s1 >= 50:
            return True
        else:
            return False
