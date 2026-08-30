class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        
        m1 = nums.index(min(nums))
        m2 = nums.index(max(nums))

        i , j = min(m1 , m2) , max(m1 , m2)

        #from front 

        f = j+1

        #from back 

        b = n- i 

        #both 

        s = (i+1) + (n-j)


        x = min(f , b , s)


        return x