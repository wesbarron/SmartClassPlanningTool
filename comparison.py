


def compareScheduleToCases(schedule, caseSchedules):
    highestMatchScore = 0
    caseWithHighestMatchScore = caseSchedules[highestMatchScore]
    for caseSchedule in caseSchedules:
        matchScore = compareScheduleToCase(schedule, caseSchedule)
        if(matchScore > highestMatchScore):
            highestMatchScore = matchScore
            caseWithHighestMatchScore = caseSchedule
    print(highestMatchScore)
    return caseWithHighestMatchScore

def compareScheduleToCase(schedule, caseSchedule):

    numOfSemesters = findNumOfSemesters(schedule)
    matchScore = 0
    for x in range(0,numOfSemesters):
        semester = schedule[x]
        if(len(semester)==0):
            semester = schedule[x+1]
        caseSemester = caseSchedule[x-numOfSemesters]
        matchScore += compareCourses(semester, caseSemester)
    return matchScore

def compareCourses(semester, caseSemester):
    numOfMatches = 0
    for x in range(0,len(semester)): #x axis
        for y in range(0,len(caseSemester)): #y axis
            if(semester[x].CourseNum == caseSemester[y]):
                numOfMatches += 1
    return numOfMatches

def findNumOfSemesters(schedule):
    count = 0
    for semester in schedule:
        if(len(semester)!=0):
            count += 1
    return count

def GetCaseSchedulesFromTrack(caseSchedulesAll, userTrack):
    return caseSchedulesAll[userTrack]


