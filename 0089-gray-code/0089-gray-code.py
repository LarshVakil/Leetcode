class Solution:
    def grayCode(self, n: int) -> list[int]:
        #gray code if i have b0b1b2b3 we turn it into gray code by bo xor b1 for g0 and use that formula 

        return [i ^ (i >> 1) for i in range(1 << n)]
        