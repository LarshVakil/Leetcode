class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        #Because of hint 1 making the set
        myset = set(friends)
        output = []

        for i in order:
            if i in myset:
                output.append(i)
        return output 
