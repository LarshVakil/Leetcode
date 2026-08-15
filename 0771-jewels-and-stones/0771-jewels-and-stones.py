class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jew_set = set(jewels)
        num = 0 

        for i in stones:
            if i in jew_set:
                num += 1 
        
        return num 