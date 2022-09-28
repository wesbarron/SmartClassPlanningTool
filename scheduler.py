import networkx as nx
import courseParser



def setSchedule(creditHours, CoursesDict):
    print("Setting Schedule: ")
    coursesInSchedule = []
    coursesChecklist = []
    Survey = CoursesDict["CPSC 4000"]

    for course in CoursesDict: 
        if course != Survey:
            coursesChecklist.append(CoursesDict[course])

    schedule = []
    
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
                        print("Course is being appended: " + course.CourseNum)
                        poppedCourseIndexes.append(i)
                        newSemester.append(course)
                        semesterCreditHours += course.CreditHours
                        coursesInSchedule.append(course)
            else:
                poppedCourseIndexes.append(i)
            poppedCourseIndexes.sort(reverse=True)

        
        if(len(newSemester)!=0):
            for index in poppedCourseIndexes:
                coursesChecklist.pop(index)
        
            for courseInSemester in newSemester:
                courseInSemester.Completed = True
            
            schedule.append(newSemester)
        
            print("New semester")


    


        
    
        
    print(schedule)
    for semester in schedule:
        print("New Semester")
        for course in semester:
            coursePrereqStr = ""
            for prereqCourse in course.prereq:
                coursePrereqStr += prereqCourse.CourseNum
            
            print(course.CourseNum + " : " + str(course.CreditHours) + " : " + coursePrereqStr)
    