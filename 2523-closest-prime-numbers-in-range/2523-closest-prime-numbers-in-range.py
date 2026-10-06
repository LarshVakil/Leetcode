class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        #prime or not by sieve oferasthonesis done in 2days back problem 

        dp = [True] * (right + 1)
        dp[0] = dp[1] = [False]

        for i in range(2 , int(right**0.5)+1):
            if dp[i] == True:
                for j in range(i*i , right+1 , i):
                    dp[j] = False
                
        primes =[i for i in range(left , right+1) if dp[i] == True]

        if len(primes) < 2:
            return [-1,-1]
        
        min_diff = float('inf')
        ans = [-1 ,-1]

        for i in range(1 , len(primes)):
            diff = primes[i]-primes[i-1]
            if diff < min_diff:
                min_diff = diff
                ans = [primes[i-1] , primes[i]]

            if min_diff <=2 :
                return ans
                
        return ans
            