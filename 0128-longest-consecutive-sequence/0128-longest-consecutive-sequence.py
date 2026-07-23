class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # count = 1
        # max = 1
        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i+1] == nums[i] + 1:
        #         count += 1
        #         if max < count:
        #             max = count
        # return max


        #For o(n) use hashset
        
        numset = set(nums)
        longest = 1

        if len(nums) == 0 :
            return 0
        #if using i in nums time > i in numset because of duplicates
        for i in numset:
            #checking start of sequence
            if i - 1 not in numset:
                length  = 1
                while (length  + i) in numset:
                    length += 1 
                    if longest < length :
                        longest = length
        return longest