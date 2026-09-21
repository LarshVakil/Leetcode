class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        hashm = {}
        c = 0

        for i , n in enumerate(s):
            hashm[n] = i

        for i in range(len(t)):
            x = hashm[t[i]]
            c += abs(x-i)

        return c 