class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        x = 0 
        y = 0 
        z = 0
        l = len(grid)
        for i in range(l):
            for j in range(l):
                if grid[i][j] != 0:
                    z += 1

        for i in range(l):
                y += max(grid[i][j] for j in range(l))
        
        for j in range(l):
                x += max(grid[i][j] for i in range(l))
            

        return x + y +z