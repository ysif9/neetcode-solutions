# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair], s=None, e=None) -> List[Pair]:
        if s is None:
            s = 0
            e = len(pairs) - 1

        if e-s <= 0:
            return pairs
        
        l = s
        pivot = pairs[e]
        for i in range(s, e):
            if pairs[i].key <  pivot.key:
                t = pairs[l]
                pairs[l] = pairs[i]
                pairs[i] = t
                l += 1
        
        t = pairs[l]
        pairs[l] = pairs[e]
        pairs[e] = t

        self.quickSort(pairs, s, l-1)
        self.quickSort(pairs, l+1, e)

        return pairs
        