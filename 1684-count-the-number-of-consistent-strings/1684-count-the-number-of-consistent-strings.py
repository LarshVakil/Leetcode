class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        sets = set(allowed)
        ans = sum(set(i).issubset(sets) for i in words)

        return ans