class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        curr = 2
        ans = 2

        n = len(nums)

        for i in range(2 , n):
            if nums[i] == nums[i-1] + nums[i-2]:
                curr += 1
            else :
                curr  = 2 
            ans = max(ans , curr)

        return ans 