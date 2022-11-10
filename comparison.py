
case1semester1 = ["ENGL 1101", "Math 1113", "Foreign Language GE", "CPSC 1301K", "KINS 1106"]
case1semester2 = ["ENGL 1102","MATH 2125","CPSC 1302","CPSC 2105","Fine Arts GE", "ITDS 1779"]
case1semester3 = ["MATH 5125U","CPSC 2108", "CYBR 2159", "Humanities GE", "Science Lab GE"]
case1semester4 = ["CPSC 3175","CPSC 2160", "STAT 1401", "HIST 2111", "Science Lab GE"]
case1semester5 = ["CPSC 3125", "CPSC 3131", "POLS 1101", "Social Sciences GE", "CPSC 4130E", "PEDS GE"]
case1semester6 = ["CPSC 3165", "CPSC 4135", "CPSC 3121", "Social Sciences GE", "GE"]
case1semester7 = ["CPSC 4175", "CPSC 4115", "CPSC 4157", "CPSC 4155", "GE"]
case1semester8 = ["CPSC 4176", "CPSC 4148", "CPSC 4000", "CPSC 4138E", "GE"]
case1 = [case1semester1,case1semester2,case1semester3,case1semester4,case1semester5,case1semester6,
case1semester7,case1semester8] #semesters
caseLibrary = [case1]
caseLibraryMatchScores = []

def compareScheduleToCases(schedule):
    numOfSemesters = findNumOfSemesters(schedule)
    matchScore = 0
    for x in range(0,numOfSemesters):
        semester = schedule[x]
        if(len(semester)==0):
            semester = schedule[x+1]
        caseSemester = case1[x-numOfSemesters]
        matchScore += compareCourses(semester, caseSemester)
    print(matchScore)
    return matchScore

def compareCourses(semester, caseSemester):
    numOfMatches = 0
    for x in range(0,len(semester)): #x axis
        for y in range(0,len(caseSemester)): #y axis
            print(semester[x].CourseNum + " == " + caseSemester[y])
            if(semester[x].CourseNum == caseSemester[y]):
                numOfMatches += 1
    return numOfMatches

def findNumOfSemesters(schedule):
    count = 0
    for semester in schedule:
        if(len(semester)!=0):
            count += 1
    return count