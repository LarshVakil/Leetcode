class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        words = set()
        
        for i in sentences :
            count = len(i.split())
            words.add(count)

        return max(words)