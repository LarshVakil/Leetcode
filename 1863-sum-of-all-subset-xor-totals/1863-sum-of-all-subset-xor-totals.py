class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        s = 0 
        n = len(nums)
        for i in range(n):
            s |= nums[i]
        
        return s * pow(2 , n-1)