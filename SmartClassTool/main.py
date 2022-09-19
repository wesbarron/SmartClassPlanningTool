import courseParser
import DAGParser
import scheduler
 
file_path = "./Sample_Input2.pdf"

fileLines = courseParser.getContent(file_path)
Courses = DAGParser.createCourses()
graph = Courses["graph"]
scheduler.findCoursesNeeded(Courses, fileLines)
defaultCreditHours = 15
scheduler.setSchedule(defaultCreditHours, Courses)

