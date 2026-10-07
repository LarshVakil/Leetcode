class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        # x = 0 
        # y = 0 
        # z = 0
        # l = len(grid)
        # for i in range(l):
        #     for j in range(l):
        #         if grid[i][j] != 0:
        #             z += 1

        # for i in range(l):
        #         y += max(grid[i][j] for j in range(l))
        
        # for j in range(l):
        #         x += max(grid[i][j] for i in range(l))
            

        # return x + y +z
        ans = 0
        ans  += sum(v > 0 for row in grid for v in row) #xy
        ans += sum(max(row) for row in grid)#yz
        ans += sum(max(col) for col in zip(*grid))#zx
        #transpose of matrix is zip(*grid)

        return ans