import networkx as nx
import courseParser
import CaseCreator
import comparison
import conversions

def setSchedule(creditHours, startingSemester, CoursesDict):
    print("Setting Schedule: ")
    coursesInSchedule = []
    coursesChecklist = []
    Survey = CoursesDict["CPSC 4000"]
    currentSemesterTime = startingSemester

    for course in CoursesDict: # put courseDict into a temporary List
        if course != Survey:
            coursesChecklist.append(CoursesDict[course])

    schedule = []
    
    while(len(coursesChecklist)>0): # while there are still courses on the list to take
        semesterCreditHours = 0
        newSemester = []
        poppedCourseIndexes = []
        for i in range(0, len(coursesChecklist)): # go through every course that needs to be taken
            course = coursesChecklist[i]
            
            
            if(course.Completed == False):
                if((semesterCreditHours + course.CreditHours)<=creditHours): # it has exceeded the credit hour limit and will not be added to this semester
                    
                    if course.canBeTaken(): # all prerequesities of course are met
                        
                        if(course.semesterTimeIsAvailable(currentSemesterTime)): # course is available during that semester 
                            print("Course is being appended: " + course.CourseNum)
                            poppedCourseIndexes.append(i)
                            newSemester.append(course)
                            semesterCreditHours += course.CreditHours
                            coursesInSchedule.append(course)
            else: # course is already completed and does not need to be put in the schedule
                poppedCourseIndexes.append(i)
            poppedCourseIndexes.sort(reverse=True)

        
        #if(len(newSemester)!=0): # this line of code is here to keep it from infinitely creating semesters, but does not fix infinite looping
        for index in poppedCourseIndexes:
            coursesChecklist.pop(index) 
    
        for courseInSemester in newSemester:
            courseInSemester.Completed = True
        
        schedule.append(newSemester)
        currentSemesterTime = setNextSemesterTime(currentSemesterTime)
        print(currentSemesterTime + " semester")
        
            


    


        
    
        
    print(schedule)
    semesterTimes = ["Fall", "Spring", "Summer"]
    i = 0
    for semester in schedule: # print to show schedule in the terminal
        print(semesterTimes[i%3] + " Semester -------------------------")
        for course in semester:
            coursePrereqStr = ""
            for prereqCourse in course.prereq:
                coursePrereqStr += str(prereqCourse.CourseNum)
            
            print(course.CourseNum + " : " + str(course.CreditHours) +" : "+ str(course.SemesterAvailability) +" : " + coursePrereqStr)
        i += 1

    return schedule

def setNextSemesterTime(currentSemesterTime):
    if currentSemesterTime == "Fall":
        return "Spring"
    elif currentSemesterTime == "Spring":
        return "Summer"
    elif currentSemesterTime == "Summer":
        return "Fall"
    else:
        return "No Semester Time" # error check

def createNewScheduleFromCaseLibrary(schedule, track):
        caseSchedulesWithAllTracks = CaseCreator.createCaseSchedules("./Cases.xlsx")
        caseSchedules = comparison.GetCaseSchedulesFromTrack(caseSchedulesWithAllTracks, track)
        caseScheduleWithHighestScore = comparison.compareScheduleToCases(schedule, caseSchedules)

        schedule = conversions.replaceElectives(schedule, caseScheduleWithHighestScore)
        return schedule