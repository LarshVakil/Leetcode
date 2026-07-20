class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        #Remote type question 2 buttons
        hash = {'--X' : -1 , 'X--': -1 , 'X++': 1 ,'++X' : 1 }

        for i in range(len(operations)):
            if operations[i] in hash :
                X += hash[operations[i]]
        return X 