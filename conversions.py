import courseParser;

def replaceElectives(schedule, caseSchedule):
    caseElectives = []
    caseElectivesIndex = 0
    for semester in caseSchedule:
       for course in semester:
        if course[-1] == 'E' and course[-2] != 'G':
            caseElectives.append(course)
    
    for semester in schedule:
        for x in range(0,len(semester)):
            if "Elective" in semester[x].CourseNum and ('CYBR' in semester[x].CourseNum or 'CPSC' in semester[x].CourseNum):
                semester[x] = caseElectives[caseElectivesIndex][:-1] + " Elective"
                if not (caseElectivesIndex + 1 > len(caseElectives)):
                    caseElectivesIndex += 1
    return schedule
def printSchedule(schedule):
    for semester in schedule:
        for course in semester:
            if(isinstance(course,str)):
                print(course)
            elif (isinstance(course, courseParser.Course)):
                print(course.CourseNum)