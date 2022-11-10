import courseParser
import scheduler
import os
import comparison
 
#file_path = r'C:\Users\Katie\Downloads\SmartClassTool\SmartClassTool\xx\Sample_Input3.pdf'
file_path = './Sample_Input4.pdf'

print("Starting parser")
parsed = courseParser.getContent(file_path)
CoursesDict= courseParser.createFromParse(parsed)
CoursesDict = courseParser.readXL("./CPSCXL.xlsx", CoursesDict)

#for course in CoursesDict:
    #courseObject = CoursesDict[course]
    #coursePrereqStr = ""
    #for prereqCourse in courseObject.prereq:
                #coursePrereqStr += prereqCourse.CourseNum
    #print(courseObject.CourseNum + "Prereqs: " +coursePrereqStr)

defaultCreditHours = 15
startingSemester = "Fall" 
schedule = scheduler.setSchedule(defaultCreditHours, startingSemester, CoursesDict)

comparison.compareScheduleToCases(schedule)

