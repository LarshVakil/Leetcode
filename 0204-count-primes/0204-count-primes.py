class Solution:
    def countPrimes(self, n: int) -> int:
        # if n<= 2:
        #     return 0
        # c = 0 
        # for i in range(2,n):
        #     for j in range(2 , int(i**0.5)+1):
        #         if i%j == 0:
        #             break 
        #     else:
        #         c += 1 
        
        # return c
        #TLE w/o sieve of eratosthenes HINT 3 

        if n <= 2 :
            return 0 
        
        #Make a array of size n with true and false as values

        dp = [True]* n
        dp[0] = dp[1] = False

        #checking primes only till sqrt of n becs any composite number less than n must have a prime factor <= sqrt n 
        for i in range(2 , int(n**0.5)+1):
            if dp[i] == True:
                #starting from i^2 because smaller multiples were already marked in increments of i 
                for j in range(i*i , n ,i):
                    dp[j] = False

                
        return sum(dp)




