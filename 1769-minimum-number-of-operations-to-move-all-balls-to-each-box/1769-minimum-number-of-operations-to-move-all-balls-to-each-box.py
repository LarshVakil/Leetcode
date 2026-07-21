class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0] * n 
        for i in range(n):
            for j in range(n):
                op = 0
                if int(boxes[j]) == 1:
                    op = i - j
                    ans[i] += abs(op)
        
        return ans
