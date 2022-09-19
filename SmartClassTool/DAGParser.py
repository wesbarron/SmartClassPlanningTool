import networkx as nx

class Course:
    def __init__(self,CourseNum, Title, CreditHours, SemestersOffered):
        self.CourseNum = CourseNum
        self.Title = Title
        self.CreditHours = CreditHours
        self.SemestersOffered = SemestersOffered # = [fall, spring, summer] in binary form, 1 meaning it is offered and 0 meaning it is not offered
        self.Needed = False
        self.Completed= False

def createCourses():
    #Create Course Objects
    C1301K = Course("1301K", "CPSC", 3, [1,1,1])
    C2105 = Course("2105", "CPSC", 3, [1,1,1])
    C2159 = Course("2159", "CYBR", 3, [1,1,0])
    C1302 = Course("1302", "CPSC", 3, [1,1,1])
    C2106 = Course("2106", "CYBR", 3, [1,1,1])
    C3121 = Course("3121", "CPSC", 3, [0,1,0])
    C5155 = Course("5155", "CPSC", 3, [1,0,0])
    C3000 = Course("3000", "CPSC", 3, [1,1,0])
    C3131 = Course("3131", "CPSC", 3, [1,1,0])
    C1113 = Course("1113", "MATH", 3, [1,1,1])
    C2125 = Course("2125", "MATH", 3, [1,1,1])
    C5125 = Course("5125", "MATH", 3, [1,1,1])
    C2108 = Course("2108","CPSC", 3, [1,1,1])
    C3175 = Course("3175", "CPSC",3, [1,1,0])
    C3125 = Course("3125", "CPSC", 3, [1,1,0])
    C5135 = Course("5135", "CPSC", 3, [0,1,0])
    C5115 = Course("5115", "CPSC", 3, [1,0,0])
    C4175 = Course("4175", "CPSC", 3, [1,0,0])
    C5157 = Course("5157", "CPSC", 3, [1,0,1])
    C5128 = Course("5128", "CPSC", 3, [0,1,0])
    C4176 = Course("4176", "CPSC", 3, [0,1,0]) 
    C4000 = Course("4000", "CPSC", 3, [1,1,1]) # has to be taken last semester




    #Create DAG
    graph = nx.DiGraph()
    graph.add_edges_from([(C1301K,C2105),(C1301K,C2159),(C1301K,C1302),(C1301K,C2106),(C1302,C3131),(C2105,C3121),(C3121,C5155),(C2105,C3125),(C2159, C5157),(C1302, C2108),
    (C1113,C2125),(C2125,C5125), (C2125,C2108),(C2108,C3125),(C2108,C3175),(C3175,C5135),(C3175,C4175),(C4175,C4176),(C2108,C5157),(C2108,C5115),(C5125,C5115),(C5115,C5128)])

    print(nx.shortest_path(graph,C1301K,C5115))
    print(nx.bfs_layers(graph,C1301K))
    #Prints Course Number in order they are traversed in BFS and adds them to dictionary (CourseNum : CourseObj)
    layers = dict(enumerate(nx.bfs_layers(graph, [C1301K, C1113])))
    Courses = dict()
    for x in layers:
        for y in layers[x]:
            print(y.CourseNum)
            Courses[y.CourseNum] = y
    Courses[C4000.CourseNum]= C4000
    Courses[C3000.CourseNum] = C3000
    Courses["graph"] = graph
    return Courses