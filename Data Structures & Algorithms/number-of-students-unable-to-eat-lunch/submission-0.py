class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        size = len(students)
        while (size > 0):
            if students[0] == sandwiches[0]:
                students = students[1::]
                sandwiches = sandwiches[1::]
                size = len(students)
            else:
                t = students[0]
                students = students[1::]
                students.append(t)
                size -= 1
        return len(students)