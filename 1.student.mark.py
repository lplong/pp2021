    #Name it «1.student.mark.py»
    #Use tuples, dicts, lists, NO objects/classes
    #Build a student mark management system


#Input functions:
    #Input number of students in a class
    #Input student information: id, name, DoB
    #Input number of courses
    #Input course information: id, name
    #Select a course, input marks for student in this course

#Listing functions:
    #List courses
    #List students
    #Show student marks for a given course



#list
studentList = []
courseList = []
markList = []

#input user selection

def selection ():
    while True:
        firstSl = print("1.Student Info")
        secondSl = print("2.Course Info")
        thirdSl = print("3.Mark Info")
        fourthSl = print("4.Exit")
        
        mySl = input("My Choice: ")    
        
        if mySl == "1":
            return studentInput()
        elif mySl == "2":
            return courseInput()
        elif mySl == "3":
            return markInput()  
        elif mySl == "4":
            break

#input student info 
def studentInput():
    studentNum = input("Enter numbers of student: ")
    for i in range(int(studentNum)):    
        studentName = input("Enter Student Name:")
        studentID = input("Enter Student ID: ")
        studentDOB = input("Student's DOB:")
        studentList.append({'student Name':studentName, 'studentID':studentID, 'student DOB': studentDOB}) 
    print(studentList)


#input course info 
def courseInput():
    courseNum = input("Enter number of courses: ")
    for j in range(int(courseNum)):
        courseName = input("Enter course name:")
        courseInfo = input("ID: ")
        courseList.append({'course name':courseName, 'ID':courseInfo}) 
    print(courseList)
 
#input grade 
def markInput():
        inputID = input("enter Student ID: ")
        inputCourse = input ("Course: ")
        inputMark = input("Mark: ")
        markList.append({'ID':inputID, 'Course':inputCourse, 'Mark':inputMark})
        print(markList)
    

    


selection()




