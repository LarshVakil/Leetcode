class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x 

        if target == 0:
            return len(nums)
        if target < 0 :
            return -1
        hashm = {0:-1}
        csum = 0 
        mlen = -1 

        for i , num in enumerate(nums):
            csum += num 
        
            if csum - target in hashm:
                mlen = max(mlen , i - hashm[csum - target])
            if csum not in hashm:
                hashm[csum] = i 

        if mlen != -1:
            return len(nums) - mlen
        else:
            return -1