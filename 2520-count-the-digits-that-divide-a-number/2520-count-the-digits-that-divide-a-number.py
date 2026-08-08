class Solution:
    def countDigits(self, num: int) -> int:
        number = 0 
        nums = str(num)

        for i in range(len(nums)):
            if num % int(nums[i]) == 0 :
                number += 1 
        
        return number 