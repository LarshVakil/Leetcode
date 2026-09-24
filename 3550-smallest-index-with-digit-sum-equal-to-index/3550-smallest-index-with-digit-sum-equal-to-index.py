class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            x = str(nums[i])
            total = 0 
            for j in x :
                total += int(j)
            if total == i :
                return i 
        return -1

           