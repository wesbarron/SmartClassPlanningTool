from PyPDF2 import PdfFileReader, PdfFileWriter
from RequiredCourses import RequiredCourse
import json

def isAreaLine(line):
    validAreas = ['area f', 'area g: program req', 'area h: track req']
    return line.lower().strip() in validAreas

def parseLine(requirement, courses):
    completed = False
    requirementName = ""
    requiredNumber = 0
    courseList = []
    completed = not requirement.endswith('Still Needed:')
    requirementName = requirement.replace('Still Needed:', '').strip()
    courseLineContent = courses.strip().split()
    requiredNumber = courseLineContent[0]
    courseList = ' '.join(courseLineContent[3:]).split(' or ')
    return RequiredCourse(completed, requirementName, requiredNumber, courseList)





def getContent(filePath):
    requirements = []
    pdf = PdfFileReader(filePath)
    requirement = None
    courses = None

    for pageNum in range(pdf.numPages):
        pageObj = pdf.getPage(pageNum)
        txt = pageObj.extractText()
        addLine = False;
        for line in txt.splitlines():
            if line.startswith("AREA"):
                if isAreaLine(line):
                    addLine = True
                    continue
                else:
                    addLine = False
            if addLine and not line.startswith("Remark"):
                if requirement is None:
                    requirement = line
                else:
                    courses = line
            if requirement is not None and courses is not None:
                requirements.append(parseLine(requirement, courses))
                requirement = None
                courses = None
    return requirements


for requiredCourse in getContent('Sample_Input2.pdf'):
    print(requiredCourse.toString())
