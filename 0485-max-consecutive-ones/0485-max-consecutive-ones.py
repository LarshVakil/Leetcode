class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # c= 0 
        # c1 = 0 
        # for i in range(len(nums) - 1):
        #     if nums[i] == 1 and nums[i+1] == 1:
        #         if c == 0 :
        #             c+= 2
        #             if c >= c:
        #                 c1 = c 
                    
        #         else: 
        #             c += 1
        #             if c1 < c :
        #                 c1 =  c
        #     if nums[i] == 1 and nums[i+1] == 0 :
        #         c = 0 
            
            
        # return c1 

        #sliding window 
    
        l = 0
        r = 0 
        longest = 0 
        n = len(nums)

        while r < n :
            if nums[r] == 0:
                l = r + 1 
                r += 1
            else : 
                w = r - l + 1 
                longest = max(w , longest) 
                r += 1

        return longest
            
           
            