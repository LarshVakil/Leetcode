class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()
        d = arr[1] - arr[0]
        a = arr[0] 
        c = 0 

        for i in range(len(arr)):
            if arr[i] == a + (i)*d:
                c+= 1 
        
        if c == len(arr):
            return True 
        else :
            return False
