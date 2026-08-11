class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        seq = nums[0]
        for i in range(1 , len(nums)):
            if nums[i] == nums[i-1] + 1 :
                seq += nums[i]
            else:
                break

        numset = set(nums)

        ans = seq
        while ans in numset:
            ans+= 1 

        return ans
            