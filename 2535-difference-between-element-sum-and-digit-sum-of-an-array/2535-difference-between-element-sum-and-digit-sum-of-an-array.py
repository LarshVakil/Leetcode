class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        summ = sum(nums)
        d_sum  = sum(int(digit) for num in nums for digit in str(num))

        return abs(summ - d_sum)

            
