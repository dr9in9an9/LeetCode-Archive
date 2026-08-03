class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        for interation in range(0, (len(students) * len(sandwiches))):
            for student in students:
                if sandwiches[0] == students[0]:
                    sandwiches.pop(0)
                    students.pop(0)
                else:
                    students.append(students.pop(0))
            
        return len(students)
