class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        hashmap = {}
        output = 0

        for char in str(n):
            if char in hashmap :
                hashmap[char] += 1
            else:
                hashmap[char] = 1 
        
        for char in hashmap :
            output += int(char) *hashmap[char]

        return output
        