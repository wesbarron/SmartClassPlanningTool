import courseParser
import scheduler
import os
import comparison
import CaseCreator
import conversions
 
#file_path = r'C:\Users\Katie\Downloads\SmartClassTool\SmartClassTool\xx\Sample_Input3.pdf'
file_path = './Sample_Input2.pdf'

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

#Case Based Implementation
caseSchedulesWithAllTracks = CaseCreator.createCaseSchedules("./Cases.xlsx") #dictionary with keys based on track
track = "SoftwareTrack" #User will define this in Front End

caseSchedules = comparison.GetCaseSchedulesFromTrack(caseSchedulesWithAllTracks, track)
caseScheduleWithHighestScore = comparison.compareScheduleToCases(schedule, caseSchedules)

schedule = conversions.replaceElectives(schedule, caseScheduleWithHighestScore)
conversions.printSchedule(schedule)



conversions.buildSchedule(schedule, defaultCreditHours, "schedule1.xlsx")

#Second excel output


print("Starting parser 2")
parsed2 = courseParser.getContent(file_path)
CoursesDict2= courseParser.createFromParse(parsed2)
CoursesDict2 = courseParser.readXL("./CPSCXL.xlsx", CoursesDict2)

schedule2 = scheduler.setSchedule(defaultCreditHours, startingSemester, CoursesDict2)
caseSchedulesWithAllTracks = CaseCreator.createCaseSchedules("./Cases.xlsx") #dictionary with keys based on track
track2 = "WebTrack" #User will define this in Front End
caseSchedules2 = comparison.GetCaseSchedulesFromTrack(caseSchedulesWithAllTracks, track2)
caseScheduleWithHighestScore2 = comparison.compareScheduleToCases(schedule2, caseSchedules2)
schedule2 = conversions.replaceElectives(schedule2, caseScheduleWithHighestScore2)

conversions.buildSchedule(schedule2, defaultCreditHours, "schedule2.xlsx")
