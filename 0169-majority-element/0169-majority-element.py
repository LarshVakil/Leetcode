class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashm = {}

        for i in nums:
            hashm[i] = hashm.get(i , 0) + 1 

            if hashm[i] > len(nums)//2 :
                return i
            
