import courseParser

def test_hours_fx():
    course = courseParser.Semester("Fall 2022", 6)
    assert course.MaxHours == 6

def test_term_fx():
    course = courseParser.Semester("Fall 2022", 6)
    assert course.Term == "Fall 2022"

def test_can_be_taken():
    course = courseParser.Course("CPSC 4175", 3, True)
    assert course.canBeTaken() == True
    
def test_is_complete():
    course = courseParser.Course("CPSC 4175", 3, True)
    assert course.isComplete() == True

    
