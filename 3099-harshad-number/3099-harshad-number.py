class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        y = str(x)
        sum = 0 

        for i in range(len(y)):
            sum += int(y[i])
        

        if x%sum == 0 :
            return sum 
        else:
            return -1