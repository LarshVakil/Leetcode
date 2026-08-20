class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        wav = 0 
        
        for i in range(num1 , num2  + 1):
            s= str(i) 
            if len(s) < 3:
                pass
            
            for j in range(1 , len(s) - 1):

                if s[j] > s[j-1] and s[j] > s[j+1]:
                    wav += 1
                elif s[j] < s[j-1] and s[j] < s[j+1] :
                    wav += 1
            
        return wav
        
        

