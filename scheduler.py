import networkx as nx
import re
import courseParser
import worksheet
import GUI
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Color, PatternFill, Font, Border
from openpyxl.styles import colors
from openpyxl.cell import Cell

def getTotalCreditHours(creditHours, CoursesDict):
    coursesInSchedule = []
    coursesChecklist = []
    Survey = CoursesDict["CPSC 4000"]
    if Survey:
        print("SEMESTER COUNT RETRIEVED")
    for course in CoursesDict: 
        if course != Survey.CourseNum:
            coursesChecklist.append(CoursesDict[course])

    schedule = []
 
    #while(len(coursesChecklist)>0):
    semesterCreditHours = 0
    newSemester = []
    poppedCourseIndexes = []
    for i in range(0, len(coursesChecklist)):
        #if credit hours limit is hit
        course = coursesChecklist[i]
        
        if(course.Completed == False):
            if((semesterCreditHours + course.CreditHours)<=creditHours):
                
                if course.canBeTaken():
                    #print("Course is being appended: " + course.CourseNum)
                    poppedCourseIndexes.append(i)
                    newSemester.append(course)
                    semesterCreditHours += course.CreditHours
                    coursesInSchedule.append(course)
    #print (semesterCreditHours)
    return semesterCreditHours

def setSchedule(creditHours, CoursesDict):
    print("Setting Schedule: ")
    coursesInSchedule = []
    coursesChecklist = []
    coursesInWorkBook = []

    for course in CoursesDict: 
       
        coursesChecklist.append(CoursesDict[course])

    schedule = []

    #print schedule

    wb = load_workbook('schedule.xlsx', keep_vba=True)
    ws = wb.active
    #ws.title = "Path To Graduation"
    ws.column_dimensions['A'].width = 25
    ws.column_dimensions['B'].width = 20
    ws.column_dimensions['C'].width = 25
    ws.column_dimensions['D'].width = 20
    ws.column_dimensions['E'].width = 25
    ws.column_dimensions['F'].width = 20
    ws.sheet_view.showGridLines = True
    # redFill = PatternFill(start_color='FFFF0000',
    #                end_color='FFFF0000',
    #                fill_type='solid')
    hoursCount = GUI.globalHoursCount
    print(getTotalCreditHours(hoursCount, CoursesDict))
    creditHoursAllowed = getTotalCreditHours(hoursCount, CoursesDict)

    
    while(len(coursesChecklist)>0):
        semesterCreditHours = 0
        newSemester = []
        poppedCourseIndexes = []
        workBookHours = 0
        logHours = 0
    
        for i in range(0, len(coursesChecklist)):
            #if credit hours limit is hit
            course = coursesChecklist[i]
            
                    
            if(course.Completed == False):
                if((semesterCreditHours + course.CreditHours)<=creditHours):
                    for prereqCourse in course.prereq:
                        for courseInSchedule in coursesInSchedule:
                            if(prereqCourse == courseInSchedule): #if prereq course is in schedule already
                                #if prereq course is in this semester, it cannot be taken
                                exists = courseInSchedule in newSemester
                                if(exists == False): #else it is in previous semester, it can be taken
                                    prereqCourse.Completed = True
                    print(course.canBeTaken())
                    if course.canBeTaken():
                        print("Course is being appended: " + course.CourseNum)
                        poppedCourseIndexes.append(i)
                        newSemester.append(course)
                        semesterCreditHours += course.CreditHours
                        coursesInSchedule.append(course)
                        coursesInWorkBook.clear()

                        if ((logHours + course.CreditHours) <= creditHoursAllowed):
                            j = i + 1
                            ws.cell(j+1,1).value = course.CourseNum
                            ws.cell(j+1,2).value = course.CreditHours
                            #print("This is the course number : " + course.CourseNum)
                            workBookHours += course.CreditHours
                            coursesInWorkBook.append(course.CourseNum)
                            
                        logHours = workBookHours + course.CreditHours
                        #print("log Hours : " + str(logHours))
                        
                
            else:
                poppedCourseIndexes.append(i)
            poppedCourseIndexes.sort(reverse=True)
        if(len(newSemester)!=0):
            for index in poppedCourseIndexes:
                coursesChecklist.pop(index)
            schedule.append(newSemester)
        wb.save("scheduleResult.xlsx") 


    # if(len(coursesChecklist)>0):
    #     for course in coursesChecklist:
    #         if((semesterCreditHours+course.CreditHours)>creditHours):
    #             schedule.append(newSemester)
    #             break
    #         #Check for courses with prereqs if prereqs are in coursesInSchedule array
    #         if(len(course.prereq) > 0):
    #             for prereqCourse in course.prereq:
    #                 for courseInSchedule in coursesInSchedule:
    #                     if(prereqCourse == courseInSchedule):
    #                         exists = courseInSchedule in newSemester
    #                         if(exists == False):
    #                             #takes prereq off the prereq array
    #                             course.prereq.remove(prereqCourse)
    #         #Check for courses without prereq
    #         elif(len(course.prereq)==0):
    #             courseFromChecklist = coursesChecklist.pop(0)
    #             newSemester.append(courseFromChecklist)
    #             coursesInSchedule.append(courseFromChecklist)
    #             semesterCreditHours += course.CreditHours 

    wb.save("schedule.xlsx") 
        
    
        
    print(schedule)
    for semester in schedule:
        print("New Semester")
        for course in semester:
            coursePrereqStr = ""
            for prereqCourse in course.prereq:
                coursePrereqStr += prereqCourse.CourseNum
            
            print(course.CourseNum + " : " + str(course.CreditHours) + " : " + coursePrereqStr)
        
