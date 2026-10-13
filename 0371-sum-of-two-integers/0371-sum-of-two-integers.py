import math
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # if a == 0 :
        #     return b 
        # elif b == 0 :
        #     return a 
        # try:
        #     c = pow(math.e , a)
        #     d = pow(math.e , b)

        #     d = math.log(c*d)

        #     return int(d) 
        
        # except:
        #     if a add b >= 709 or a add b <= - 709 :
        #         # the limits are e^709 


        # Using half adder logix sum = axorb 
        #and carry = axorb  add c(a.b) = a&b << 1

        Mask = 0xFFFFFFFF
        Max = 0x7FFFFFFF

        while b!=0 :
            carry = (a & b) << 1 
            a = (a^b) & Mask
            b = carry & Mask 

        if  a <= Max:
            return a 
        else:
            return ~(a ^ Mask)


