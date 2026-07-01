class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = {}
        map_t = {}

        if len(s) != len(t) :
            return False
        
        else:

            for char in s:
                map_s[char] = map_s.get(char , 0) + 1

            for char in t:
                map_t[char] = map_t.get(char , 0) + 1  

            for key in map_s:
                if map_s[key] != map_t.get(key , 0):
                    return False

            return True
        

            

