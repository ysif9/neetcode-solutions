# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        states = []
        for i,v in enumerate(pairs):
            j = i
            while (j > 0 and pairs[j - 1].key > pairs[j].key):
                t = pairs[j]
                pairs[j] = pairs[j-1]
                pairs[j-1] = t
                j -= 1
            states.append(pairs.copy())
        return states