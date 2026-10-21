class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        seen = set()
        duplicate = -1

        for i in nums:
            if i in seen:
                duplicate = i
            else:
                seen.add(i)

        missing = -1
        for i in range(1 , n+1):
            if i not in seen:
                missing = i
                break
        return [duplicate , missing]