class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        a = max(nums)
        b = min(nums)

        c = max(0 , a-b-(2*k))

        return c 