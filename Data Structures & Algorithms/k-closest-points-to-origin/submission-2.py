import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for i,v in enumerate(points):
            # v[0] -> x
            # v[1] -> y
            dist.append((math.pow(0-v[0], 2) + math.pow(0-v[1],2), i))
        dist.sort()
        dist =  [points[v[1]] for i, v in enumerate(dist)]
        return dist[:k]