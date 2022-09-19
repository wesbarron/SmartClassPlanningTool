class RequiredCourse:
    def __init__(self, completed, requirementName, requiredNumber, courseList):
        self.completed = completed
        self.requirementName = requirementName
        self.requiredNumber = requiredNumber
        self.courseList = courseList

    def toString(self):
        return self.requirementName + "\t\t" + str(self.completed) + "\t" + self.requiredNumber + "\t" + str(self.courseList)
