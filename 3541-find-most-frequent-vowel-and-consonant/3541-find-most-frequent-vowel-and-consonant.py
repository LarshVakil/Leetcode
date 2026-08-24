class Solution:
    def maxFreqSum(self, s: str) -> int:
        from collections import Counter

        vowels = { 'a' , 'e' , 'i' , 'o' , 'u' }
        count = Counter(s)

        max_vow = 0 
        max_cons = 0 

        for i , j in count.items():
            if i in vowels:
                max_vow = max(max_vow , j)
            else :
                max_cons = max(max_cons , j )
        
        return max_cons + max_vow 

