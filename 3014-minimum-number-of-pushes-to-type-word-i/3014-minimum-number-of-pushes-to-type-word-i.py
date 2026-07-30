class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = Counter(word)
        pushes = 0 
        i = 0

        for char , freq in counts.most_common():
            if i < 8 :
                pushes += freq * 1 
            elif i < 16 :
                pushes += freq * 2 
            elif i < 24 :
                pushes += freq * 3 
            else : 
                pushes += freq * 4 

            i += 1 
            
        return pushes