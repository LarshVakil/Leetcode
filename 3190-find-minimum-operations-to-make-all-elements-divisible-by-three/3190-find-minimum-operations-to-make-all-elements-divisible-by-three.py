class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        op = 0
        for i in nums:
            if i % 3 != 0:
                # either +1 or -1 will give ans if rem is not 0 
                op += 1
        return op