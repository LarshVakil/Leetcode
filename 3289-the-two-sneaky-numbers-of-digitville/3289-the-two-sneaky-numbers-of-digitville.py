class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        hash = {}
        sneaky = []

        for i in nums:
            if i in hash:
                sneaky.append(i)
            else :
                hash[i] = 1
            
        return sneaky




           