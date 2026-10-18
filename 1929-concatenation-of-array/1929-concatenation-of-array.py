class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*(n*2)
        for ind ,num in enumerate(nums):
            ans[ind] , ans[ind + n] = num , num 
        return ans