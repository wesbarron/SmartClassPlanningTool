import networkx as nx

def findCoursesNeeded(Courses, lines):
    for x in range(len(lines)): #starting the file at line 46
        print("Courses Needed: " + lines[x])
        if("1 Class in CPSC " in lines[x] or "1 Class in CYBR " in lines[x]):
            print(lines[x])
            if("or" in lines[x]):
                courseNum = lines[x][25:29]
            else:
                courseNum = lines[x][17:21]
            
            
            if(Courses.get(courseNum)):
                Courses[courseNum].Needed = True
            
            
        
def setSchedule(creditHours, Courses):
    print("Setting Schedule: ")
    coursesChecklist = []
    graph = Courses["graph"]
    for node in nx.nodes(graph):
        if(node.Needed):
            coursesChecklist.append(node)

    
    schedule = []

    while(len(coursesChecklist)>0):
        semesterCreditHours = 0
        newSemester = []
        while semesterCreditHours<creditHours:
            if(len(coursesChecklist)>0):
                course = coursesChecklist.pop(0)
                newSemester.append(course)
                semesterCreditHours += course.CreditHours
            else:
                break
            
        schedule.append(newSemester)
    
    for semester in schedule:
        print("New Semester")
        for course in semester:
            print(course.CourseNum)
        