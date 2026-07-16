class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        #The first number is never a duplicate so taking the index as 1 
        i = 1
        for j in range (1 , n):
            if nums[j] != nums[j-1]:
            #not a duplicate 
                nums[i] = nums[j]
                i+= 1
                #at the the end i will shift only the number of times when there is a unique number and it starts from 0 
        return i
            
            
