class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # #o(n^2) soln 
        # p = 0
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i < j:
        #             if nums[i] == nums[j]:
        #                 p += 1
        #             else:
        #                 pass
        #         else:
        #             pass

        # return p 

        # o(n) - Hashmap 
        count = {}
        goodpairs =0

        for i in nums:
            if i in count:
                goodpairs += count[i]
                count[i] += 1
            else:
                count[i] = 1
        return goodpairs


        


                    