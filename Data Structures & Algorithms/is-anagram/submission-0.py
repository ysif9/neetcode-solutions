from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = Counter(s)
        counter2 = Counter(t)
        return counter == counter2