class Solution:
    def minElement(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            nums[i] = sum(int(j) for j in str(nums[i]))
        
        return min(nums)