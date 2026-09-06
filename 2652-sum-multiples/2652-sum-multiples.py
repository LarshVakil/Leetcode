class Solution:
    def sumOfMultiples(self, n: int) -> int:
        def sumdivby(k):
            x = n//k
            return k*x*(x+1)//2
        
        return( sumdivby(3) + sumdivby(5) + sumdivby(7) - sumdivby(15) - sumdivby(21) - sumdivby(35)+ sumdivby(105))        
         