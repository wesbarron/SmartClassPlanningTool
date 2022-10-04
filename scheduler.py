import re
import courseParser
import worksheet
import GUI
from openpyxl import Workbook
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
    coursesInWorkBook = []
    coursesChecklist = []
    Survey = CoursesDict["CPSC 4000"]
    if Survey:
        print("SURVEY RETRIEVED")
    for course in CoursesDict: 
        if course != Survey.CourseNum:
            coursesChecklist.append(CoursesDict[course])

    schedule = []

    #print schedule

    wb = Workbook()
    ws = wb.active
    ws.title = "Path To Graduation"
    ws.column_dimensions['A'].width = 25
    ws.column_dimensions['B'].width = 20
    ws.column_dimensions['D'].width = 25
    ws.column_dimensions['E'].width = 20
    ws.sheet_view.showGridLines = True
    redFill = PatternFill(start_color='FFFF0000',
                   end_color='FFFF0000',
                   fill_type='solid')
    hoursCount = GUI.globalHoursCount
    print(getTotalCreditHours(hoursCount, CoursesDict))
    creditHoursAllowed = getTotalCreditHours(hoursCount, CoursesDict)
    
    while(len(coursesChecklist)>0):
        semesterCreditHours = 0
        newSemester = []
        poppedCourseIndexes = []
        workBookHours = 0
        for i in range(0, len(coursesChecklist)):
            #if credit hours limit is hit
            course = coursesChecklist[i]

              
            if(course.Completed == False):
                if((semesterCreditHours + course.CreditHours)<=creditHours):
                    
                    if course.canBeTaken():
                        print("Course is being appended: " + course.CourseNum)
                        poppedCourseIndexes.append(i)
                        newSemester.append(course)
                        semesterCreditHours += course.CreditHours
                        coursesInSchedule.append(course)
                        coursesInWorkBook.clear()
                        
                        if((workBookHours + course.CreditHours)<=creditHoursAllowed):
                            j = i + 1
                            #print(semesterCreditHours)
                            poppedCourseIndexes.sort(reverse=True)
                            ws.cell(1,1).value = "New Semester"
                            ws.cell(1,2).value = "Credit Hours"
                            ws.cell(1,1).fill = redFill
                            ws.cell(1,2).fill = redFill
                            ws.cell(1,1).font = Font(color=colors.WHITE)
                            ws.cell(1,2).font = Font(color=colors.WHITE)
                            ws.cell(j+1,1).value = course.CourseNum
                            ws.cell(j+1,2).value = course.CreditHours
                            print("This is the course number : " + course.CourseNum)
                            workBookHours += course.CreditHours
                            #coursesInWorkBook.append(course.CourseNum)
                            logHours = workBookHours + course.CreditHours
                        for x in range(j+1, len(coursesInSchedule)+1):
                            #coursesInWorkBook.clear()
                            coursesInWorkBook.append(ws.cell(x,1).value)
                        #print ("Courses from the sheet " + str(coursesInWorkBook))
                                
                        # if course.CourseNum not in coursesInWorkBook:
                        #     print("Courses not in WorkBook " + course.CourseNum)
                        if course.CourseNum not in coursesInWorkBook:
                            j = i + 1
                            #print(semesterCreditHours)
                            ws.cell(1,4).value = "New Semester"
                            ws.cell(1,5).value = "Credit Hours"
                            ws.cell(1,4).fill = redFill
                            ws.cell(1,5).fill = redFill
                            ws.cell(1,4).font = Font(color=colors.WHITE)
                            ws.cell(1,5).font = Font(color=colors.WHITE)
                            ws.cell(j+1,4).value = course.CourseNum
                            ws.cell(j+1,5).value = course.CreditHours
                            #print(workBookHours+course.CreditHours)
                            print(course.CreditHours)
                            logHours += course.CreditHours
                            print(logHours)
                            
                  
            else:
                poppedCourseIndexes.append(i)
                
                       
            poppedCourseIndexes.sort(reverse=True)
            
        
        if(len(newSemester)!=0):
            for index in poppedCourseIndexes:
                coursesChecklist.pop(index)
        
            for courseInSemester in newSemester:
                courseInSemester.Completed = True
            
            schedule.append(newSemester)
        
            #print("New semester")
    newSemester.append(Survey)
    totalColumn = len(coursesInSchedule)
    ws.cell(totalColumn+3,1).value = "Total"
    ws.cell(totalColumn+3,2).value = creditHoursAllowed
    ws.cell(totalColumn+3,1).fill = redFill
    ws.cell(totalColumn+3,2).fill = redFill
    ws.cell(totalColumn+3,1).font = Font(color=colors.WHITE)
    ws.cell(totalColumn+3,2).font = Font(color=colors.WHITE)
    worksheet.set_border(ws, "A1:B"+str(totalColumn+3))

    ws.cell(totalColumn+3,4).value = "Total"
    ws.cell(totalColumn+3,5).value = creditHoursAllowed
    ws.cell(totalColumn+3,4).fill = redFill
    ws.cell(totalColumn+3,5).fill = redFill
    ws.cell(totalColumn+3,4).font = Font(color=colors.WHITE)
    ws.cell(totalColumn+3,5).font = Font(color=colors.WHITE)
    worksheet.set_border(ws, "D1:E"+str(totalColumn+3))

    

    wb.save("schedule.xlsx") 

    for semester in schedule:
        print("New Semester")
           
        for course in semester:
            print(course.CourseNum + " : " + str(course.CreditHours))
            
        
      
    