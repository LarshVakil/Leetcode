class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        out = []
        for i in range(len(words)):
            for j in range(len(words[i])):
                if words[i][j] == x :
                    out.append(i)
                    break

        return out 