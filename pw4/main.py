
class main:

    # input user selection
    def selection(self):
        while True:
            firstSl = print("1.Student Info")
            secondSl = print("2.Course Info")
            # thirdSl = print("3.Mark Info")
            fourthSl = print("4.Exit")

            mySl = input("My Choice: ")

            if mySl == "1":
                return self.studentInput()
            elif mySl == "2":
                return self.courseInput()
            # elif mySl == "3":
            #     return self.markInput()
            elif mySl == "4":
                break

    # input student info
    def studentInput(self):
        studentNum = input("Enter numbers of student: ")
        for i in range(int(studentNum)):
            studentName = input("Enter Student Name:")
            studentID = input("Enter Student ID: ")
            studentDOB = input("Student's DOB:")
            students.append(
                {'student Name': studentName, 'studentID': studentID, 'student DOB': studentDOB})
        print(students)

    # input course info

    def courseInput(self):
        courseNum = input("Enter number of courses: ")
        for j in range(int(courseNum)):
            courseName = input("Enter course name:")
            courseInfo = input("ID: ")
            courses.append({'course name': courseName, 'ID': courseInfo})
        print(courses)

    # input grade

    # def markInput(self):
    #     inputID = input("enter Student ID: ")
    #     inputCourse = input("Course: ")

    #     inputMark = input("Mark: ")
    #     x = math.floor(float(inputMark))

    #     marks.append({'ID': inputID, 'Course': inputCourse, 'Mark': x})
    #     print(marks)


my_input = Input()
my_input.selection()