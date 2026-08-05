class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        #by hint finding max and min
        mins , maxs  =  min(nums) , max(nums)
        sets = set(nums)

        return[x for x in range(mins , maxs) if x not in sets]