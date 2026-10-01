class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import itertools 

        x = [i for i in range(1,n+1)]

        permutations = list(itertools.permutations(x))

        ans_list = permutations[k-1]

        return str("".join(str(i) for i in ans_list))