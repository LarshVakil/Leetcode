class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0 

        for i in accounts:
            money = 0 
            for j in i :
                money += j

                if money > richest :
                    richest = money
        
        return richest

