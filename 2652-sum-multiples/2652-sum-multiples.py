class Solution:
    def sumOfMultiples(self, n: int) -> int:
        sum = 0
        sett = set(range(1,n+1))
        for i in sett:
            if i%3==0 or i%5==0 or i%7==0:
                sum += i 
        return sum