class domain:
    students = []
    studentsDict = []
    gpas = []


    def findGPA(studentObj):
        GPA = 0
        all_grade_points = 0
        all_credits = 0

        for course in studentObj.courses:
            grade_point = course.mark * course.credit
            all_grade_points += grade_point
            all_credits += course.credit

        GPA = all_grade_points/all_credits
        studentObj.gpa = GPA

        return GPA


    class Student():
        def __init__(self, Id, name, dob):
            self.name = name
            self.id = Id
            self.dob = dob
            self.courses = []
            self.gpa = None


    class Course():
        def __init__(self, Id, name, credit, mark):
            self.name = name
            self.id = Id
            self.mark = math.floor(float(mark))
            self.credit = credit