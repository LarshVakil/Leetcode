class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        same = []
        more = []
        for i in range(len(nums)):
            if nums[i] < pivot:
                less.append(nums[i])
            elif nums[i] == pivot:
                same.append(nums[i])
            elif nums[i] > pivot :
                more.append(nums[i])
        sol = less + same + more 
        return sol