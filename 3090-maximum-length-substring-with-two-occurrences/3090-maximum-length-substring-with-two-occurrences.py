class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        length = 0 

        for i in range(n):
            f = collections.Counter()
            for j in range(i , n):
                f[s[j]] += 1
                if f[s[j]] > 2:
                    break 

                length = max(length , j-i+1)
            
        return length

