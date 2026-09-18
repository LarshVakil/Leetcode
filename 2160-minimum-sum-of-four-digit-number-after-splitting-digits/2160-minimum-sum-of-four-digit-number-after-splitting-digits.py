class Solution:
    def minimumSum(self, num: int) -> int:
        a = list(str(num))
        a.sort()
        b = int(a[3])
        c = int(a[2])
        x = int(a[0])*10 + b
        y = int(a[1])*10 + c 

        return x + y 

