class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        left , right = 0 , len(nums) - 1
        maxi = 0
        while left < right :
            product = (nums[left] - 1 ) * (nums[right]-1)
            if product > maxi : 
                maxi = product 
            if nums[left] > nums[right]:
                right -= 1
            else:
                left += 1
        
        return maxi