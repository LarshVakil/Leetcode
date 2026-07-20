class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        out = 0
        for i in range(len(nums)):
            if i%2 == 1 :
                out -= nums[i]
            else :
                out += nums[i]
        return out 