class Solution:
    def reverse(self, x: int) -> int:
        rev = 0 
        
        if x < 0 :
            init = -1
        else:
            init = 1
        x = abs(x)
        while x > 0 :
            digit = x % 10 
            rev = rev *10 + digit 
            x = x//10
        
        if  rev*init in range(-2147483648 ,2147483647):
            return rev*init 
        else:
            return 0 