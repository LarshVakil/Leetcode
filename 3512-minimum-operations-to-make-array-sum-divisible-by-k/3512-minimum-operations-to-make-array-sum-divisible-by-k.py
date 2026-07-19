class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        sum = 0
        i = 0
        for i in range(len(nums)):
            sum += nums[i]
        
        o = (sum % k )
        
        return o 
