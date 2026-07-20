class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        letters = {}
        out = []
        for i in range(len(words)):
            total = 0
            for j in range((len(words[i]))):
                if words[i][j] in letters:
                    pass
                else:
                    letters[words[i][j]] = (ord(words[i][j]) - 97 )
            for j in range((len(words[i]))):
                total += weights[letters[words[i][j]]]
            rem = total%26

            char  = chr(ord('z') - rem)
            out.append(char)

        return "".join(out)