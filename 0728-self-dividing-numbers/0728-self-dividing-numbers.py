class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        x =[i for i in range(left,right+1)]
        ans = []

        for i in x:
            t = str(i)
            c= []
            for j in range(len(t)):
                n = int(t[j])
                if n!= 0 and i%n ==0:
                    c.append(n)
            if len(c) == len(t):
                ans.append(i)
            
        return ans

                