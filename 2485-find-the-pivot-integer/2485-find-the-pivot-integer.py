class Solution:
    def pivotInteger(self, n: int) -> int:
        ans = pow((n*(n+1))/2,1/2)

        if ans%1 == 0:
            return int(ans)
        else:
            return -1 


