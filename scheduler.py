import networkx as nx
import courseParser



def setSchedule(creditHours, CoursesDict):
    print("Setting Schedule: ")
    coursesInSchedule = []
    coursesChecklist = []

    for course in CoursesDict: 
       
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
            else:
                poppedCourseIndexes.append(i)
            poppedCourseIndexes.sort(reverse=True)
        if(len(newSemester)!=0):
            for index in poppedCourseIndexes:
                coursesChecklist.pop(index)
            schedule.append(newSemester)
        


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


        
    
        
    print(schedule)
    for semester in schedule:
        print("New Semester")
        for course in semester:
            coursePrereqStr = ""
            for prereqCourse in course.prereq:
                coursePrereqStr += prereqCourse.CourseNum
            
            print(course.CourseNum + " : " + str(course.CreditHours) + " : " + coursePrereqStr)
        