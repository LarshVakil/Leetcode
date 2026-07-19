class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)
        output = [0]*n
        
        for i in range(n):
            output[i] = sum(matrix[i])
        return output

