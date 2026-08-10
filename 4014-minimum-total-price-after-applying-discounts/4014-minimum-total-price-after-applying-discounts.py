class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse = True) 
        discounts.sort(reverse = True)

        n = len(prices)
        m = len(discounts)

        
        if m > n :
            prices += [0] * (m-n)
            costs = [0] * m 
        elif n > m :
            discounts += [0] * (n-m)
            costs = [0] * n 
        else:
            costs = [0] * n 
            
        i = max(m , n )

        for t in range(i):
            costs[t] = (prices[t] * (100 - discounts[t])) / 100

        sum = 0 
        for i in range(len(costs)):
            sum += costs[i]

        return sum
        