class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        rev = [0] * len(nums)
        for i in range(len(nums)):
            rev[i] = nums[len(nums) - 1 -i]
        concat = nums + rev 

        return concat 