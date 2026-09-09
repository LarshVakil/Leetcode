class Solution:
    def minOperations(self, n: int) -> int:
        if n%2 == 1 :
            return int(((n*n)-1)/4)
        else:
            return int((n*n)/4)


