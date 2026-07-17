from collections import Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt = Counter(students)
        res = len(students)
        for i, v in enumerate(sandwiches):
            if cnt[v] == 0:
                return res
            else:
                res -= 1
                cnt[v] -= 1
        return 0