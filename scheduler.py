import courseParser
import GUI
from openpyxl import Workbook



def setSchedule(creditHours, CoursesDict):
    print("Setting Schedule: ")
    coursesInSchedule = []
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
    ws.sheet_view.showGridLines = True
    hoursCount = GUI.globalHoursCount
    
    while(len(coursesChecklist)>0):
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
                        j = i + 1
                        print(semesterCreditHours)
                        ws.cell(1,1).value = "New Semester"
                        ws.cell(1,2).value = "Credit Hours"
                        ws.cell(j+1,1).value = course.CourseNum
                        ws.cell(j+1,2).value = course.CreditHours
                
            else:
                poppedCourseIndexes.append(i)
                print("i = "+str(i))
                #j = 1
                
                ws.cell(1,3).value = "Future Semester"
                ws.cell(1,4).value = "Credit Hours"
                ws.cell(i-7,3).value = course.CourseNum
                ws.cell(i-7,4).value = course.CreditHours
                
                    
                
            poppedCourseIndexes.sort(reverse=True)

        
        if(len(newSemester)!=0):
            for index in poppedCourseIndexes:
                coursesChecklist.pop(index)
        
            for courseInSemester in newSemester:
                courseInSemester.Completed = True
            
            schedule.append(newSemester)
        
            #print("New semester")
    newSemester.append(Survey)


    #print schedule

    # wb = Workbook()
    # ws = wb.active
    # ws.title = "Path To Graduation"
    # ws.sheet_view.showGridLines = True

    for semester in schedule:
        print("New Semester")
        # for i in range(1, len(semester)):
        #     print("i = "+str(i))
        #     ws.cell(i, 1).value = "New Semester"
        #     ws.cell(i, 2).value = "Credit Hours"
        
        for course in semester:
            print(course.CourseNum + " : " + str(course.CreditHours))
            # ws.cell(2,1).value = getattr(course, 'CourseNum')
            # ws.cell(3,1).value = getattr(course, 'CourseNum')
            # ws.cell(4,1).value = getattr(course, 'CourseNum')
            # ws.cell(5,1).value = getattr(course, 'CourseNum')
            # ws.cell(6,1).value = getattr(course, 'CourseNum')
            # ws.cell(7,1).value = getattr(course, 'CourseNum')
            # ws.cell(8,1).value = getattr(course, 'CourseNum')
            # print(getattr(course, 'CourseNum'))
            # for j in range(1, len(schedule)):
            #     print("j "+str(j))
            #     ws.cell(j,1).value = getattr(course, 'CourseNum')
            #     ws.cell(j,2).value = course.CreditHours
            #     j = j + 1
        
    wb.save("schedule.xlsx")   
    