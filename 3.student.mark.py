# Copy your practical work 2 to 3.student.mark.oop.math.py
# • Use math module to round-down student scores to 1-digit decimal upon input, floor()
# • Use numpy module and its array to
#   • Add function to calculate average GPA for a given student
#        • Weighted sum of credits and marks
#   • Sort student list by GPA descending
# • Decorate your UI with curses module




import math  
import numpy as np 
 


#list
studentList =[] 
courseList = []
markList = []
gpa = []

       


class Student:
    def __init__(self, studentID, studentName, studentDOB):
        self.__studentName = studentName
        self.__studentID = studentID
        self.__studentDOB = studentDOB
        studentList.append(self)
   
    def get_studentName(self):
        return self.__studentName
    
    def get_studentID(self):
        return self.__studentID

    def get_studentDOB(self):
        return self.__studentDOB

class Course:
    def __init__(self, courseID, courseName):
        self.__courseName = courseName
        self.__courseID = courseID
        courseList.append(self)
   
    def get_courseName(self):
        return self.__courseName
    
    def get_courseID(self):
        return self.__courseID


class Mark:
    def __init__(self, studentID, courseID, mark):
        self.__studentID = studentID
        self.__courseID = courseID
        self.__mark = mark
        markList.append(self)

    def get_studentID(self):
        return self.__studentID

    def get_courseID(self):
        return self.__courseID

    def get_mark(self):
        return self.__mark




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
        inputMark =input("Mark: ")
        markList.append({'ID':inputID, 'Course':inputCourse, 'Mark':inputMark})
        print(markList)
    

def averagegpa():
    totalPoint = input("Total Point: ")
    totalCredits = input("Total Credits: ")
    gpaPoint = math.floor(totalPoint / totalCredits)
    return gpaPoint
    print("GPA: ",gpaPoint)
    
     


selection()
averagegpa()