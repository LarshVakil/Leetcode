class Solution:
    def addBinary(self, a: str, b: str) -> str:
        dec_a = int(a , 2)
        dec_b = int(b , 2)

        c= dec_a + dec_b

        bin_c = bin(c)

        ans = bin_c[2:]

        return ans
        