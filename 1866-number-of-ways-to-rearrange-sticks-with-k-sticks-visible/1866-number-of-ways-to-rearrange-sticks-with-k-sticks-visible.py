class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        # import itertools 

        # mod = 10**9 + 7 
        # x = [i for i in range(1,n+1)]
        # perms = itertools.permutations(x)
        # c = 0

        # for i in perms:
        #     maxi = 0 
        #     v = 0 
        #     for j in i:
        #         if j > maxi :
        #             v += 1
        #             maxi = j
        #     if v == k:
        #         c+= 1
        
        # return c % mod

        #TLE :(

        mod = 10**9 + 7
        

        dp = [[0] * (k + 1) for i in range(n + 1)]
        #out of n factorial case only a max of k + 1 eill have k stick visible 
        
        dp[0][0] = 1
        
        #help used form solutions 
        for i in range(1, n + 1):
            for j in range(1, min(i, k) + 1):
                #if taking shortest stick it can be placed 2 ways its visible only if it at the begining and rest i-1 places its not visible we add the 2 cases 
                dp[i][j] = 1*(dp[i-1][j-1] + (i-1) *dp[i-1][j])%mod
                
        return dp[n][k]