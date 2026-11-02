# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(
        self, 
        p: List[Pair], 
        start: int = 0,
        end = None
    ) -> List[Pair]:
        if end is None:
            end = len(p) - 1
        if start >= end:
            return p

        s = start
        pivot = p[end].key

        for i in range(start, end):
            if p[i].key < pivot:
                p[i], p[s] = p[s], p[i]
                s += 1

        p[s], p[end] = p[end], p[s]
        self.quickSort(p, start, s - 1)
        self.quickSort(p, s + 1, end)
        return p
