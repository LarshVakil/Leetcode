class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        #n is less than 100 so 2 digit number

        while (max(1,(n//10)) * (n%10)) % t != 0:
            n += 1
        return n 