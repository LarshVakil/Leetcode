class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        hash = {'ones': 0 , 'zeros':0}
        soln = [1] * len(nums)
        for i in range(len(nums)):
            if nums[i]%2 == 0 :
                hash['zeros'] += 1 
            else :
                hash['ones'] += 1
        for i in range(0 , hash['zeros'],1):
            soln[i] = 0 
        
        return soln