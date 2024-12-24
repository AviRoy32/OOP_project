class ClassRoom:
    def __init__(self,name):
        self.name = name
        self.students = []    # list of student object
        self.subjects = []    # list of subject object

    def add_student(self,student):   #  rahim, eight e vortti hobe.
        roll_no = f"{self.name}-{len(self.students)+1}"
        student.id = roll_no
        self.students.append(student)

    def add_subject(self,subject):
        self.subjects.append(subject)

    def take_semester_final(self):
        for subject in self.subjects:
            subject.exam(self.students) 
        for student in self.students:
            student.calculate_final_grade()