# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

import math
class Solution:

    def merge(self, a1, a2):
        l = 0
        r = 0
        arr = []

        for i in range(len(a1) + len(a2)):
            if l >= len(a1):
                arr.extend(a2[r:])
                break
            elif r >= len(a2):
                arr.extend(a1[l:])
                break
            elif a1[l].key <= a2[r].key:
                arr.append(a1[l])
                l += 1
            else:
                arr.append(a2[r])
                r +=1
        return arr

    def mergeSort(self, pairs: List[Pair], s=None, e=None) -> List[Pair]:
        if s is None:
            s = 0
            e = len(pairs)
        if e-s <= 1:
            return pairs[s:e]
        
        m = (s+e) // 2
        a1 = self.mergeSort(pairs, s, m)
        a2 = self.mergeSort(pairs, m, e)

        a_f = self.merge(a1, a2)

        return a_f

