class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        s = set()

        for i in range(len(nums)):
               for j in range(nums[i][0] , nums[i][1] + 1 ):
                    s.add(j)
        
        return len(s)