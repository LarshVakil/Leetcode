class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        o = s.strip()
        i = len(o) - 1
        length = 0
        
        while i>= 0 and o[i] != " " :
            i -= 1
            length+= 1
        
        return length




        