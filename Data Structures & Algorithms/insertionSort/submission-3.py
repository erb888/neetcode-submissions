# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res = []
        lent = len(pairs)
        copy = pairs.copy()
        res.append(copy)

        if lent == 0:    
            return pairs
        elif lent == 1:
            return res

        for i in range(1, lent):
            j = i - 1
            k = i

            while (j >= 0 and pairs[k].key < pairs[j].key):
                pairs[k], pairs[j] = pairs[j], pairs[k]
                j -= 1
                k -= 1

            copy = pairs.copy()
            res.append(copy)

        return res