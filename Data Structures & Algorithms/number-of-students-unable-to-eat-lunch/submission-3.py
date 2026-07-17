from collections import Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = Counter(students)
        for i, s in enumerate(sandwiches):
            if count[s] == 0:
                return len(sandwiches) - i
            count[s] -= 1
        return 0