class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = []
        g = {}

        for i , n in enumerate(groupSizes):
            if n not in g:
                g[n] = []
            
            g[n].append(i)
        
            if len(g[n]) == n:
                ans.append(g[n])
                g[n] = []
                
        
        return ans