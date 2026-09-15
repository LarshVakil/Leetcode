class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s = sorted(nums)
        hashm = {}

        for i , n in enumerate(s):
            if n not in hashm:
                hashm[n] = i 
        
        ans = [hashm[n] for n in nums]

        return ans 