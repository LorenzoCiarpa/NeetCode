class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counter = 0
        while students and counter < len(students):

            stud = students.pop(0)

            if stud == sandwiches[0]:
                counter = 0
                sandwiches.pop(0)
            else:
                students.append(stud)
                counter += 1
        
        return len(students)