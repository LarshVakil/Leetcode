class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k%2 == 0 or k%5 == 0  :
            return -1 
        
        else:
            n = 1 
            l = 1  
            while n%k !=0 :
                n = (n*10) + 1 
                l += 1

        return l
