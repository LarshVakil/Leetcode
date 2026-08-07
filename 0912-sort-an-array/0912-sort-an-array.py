class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)   

        
        def _heapify(nums :list[int] , n:int , i :int):
            largest = i
            left , right = 2*i + 1 , 2*i + 2 
            if left <  n and nums[left] > nums[largest]:
                largest = left
            if right < n and nums[right] > nums[largest]:
                largest = right 
            if largest != i :
                nums[i] , nums[largest] = nums[largest] , nums[i] 
                _heapify(nums, n, largest)  

        for i in range(n//2 -1 , -1 ,-1 ):
            _heapify(nums , n ,i )
        for i in range(n-1 , 0 , -1):
            nums[0] , nums[i] = nums[i] , nums[0]
            _heapify(nums , i ,0)


        return nums 