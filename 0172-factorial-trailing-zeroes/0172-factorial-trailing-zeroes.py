class Solution:
    def trailingZeroes(self, n: int) -> int:
        #0-4 0 5-9 1 and so on till 25 when 25 = 5*5 so 2 zeroes 
        # so gif[n/5] + gif[n/25] .. 
        c = 0 
        if n < 5:
            return 0 
        while n >= 5 :
            c += n//5 
            n = n//5 
        return c
        
