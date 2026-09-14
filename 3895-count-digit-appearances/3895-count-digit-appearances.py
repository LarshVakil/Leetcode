class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        from collections import Counter

        hashm = Counter("".join(map(str , nums)))

        return hashm[str(digit)]

    