class Solution:
    def countDigitOne(self, n: int) -> int:
        c = 0
        i = 1 

        while i <= n :
            c += n//(i*10) *i +min(max(n % (i * 10) - i+1,0) , i)
            i *= 10
        return c
