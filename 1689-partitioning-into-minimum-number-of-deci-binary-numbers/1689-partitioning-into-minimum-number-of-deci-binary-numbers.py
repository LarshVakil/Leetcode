class Solution:
    def minPartitions(self, n: str) -> int:
        #From hints we know if there is a numer like x9x answer is 9 bcs for the digit 9 we need x1x 9 times so ans 9 so we get the max digit and thats the answer
        max = 0
        for i in range(len(n)):
            if int(n[i]) > max:
                max = int(n[i])
        return max
            