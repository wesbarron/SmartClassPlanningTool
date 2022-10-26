import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import math

from cv2 import dnn_KeypointsModel
import courseParser
import scheduler
import os


class SmartClassPlanner(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SmartClass Planning Tool")
        self.geometry("500x500")
        

        self.file = ""
        self.CrHours= IntVar()
        self.fileSelected= StringVar()
        self.fileSelected.set("No File Selected")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        fallSemester = tk.Listbox()
        sprSemester = tk.Listbox()
        sumSemester = tk.Listbox()
        self.year = 1
        self.schedule = []
        self.lastYear = False
        
        self.listBoxes = [fallSemester, sprSemester, sumSemester]
        self.CreateWidgets()

    def CreateWidgets(self):
        
        fallLabel = tk.Label(self, text="Fall Semester")
        fallLabel.grid(row=0,column=0)
        self.listBoxes[0].grid(row=1,column=0)
        sprLabel = tk.Label(self, text="Spring Semester")
        sprLabel.grid(row=0,column=1)
        self.listBoxes[1].grid(row=1,column=1)
        sumLabel = tk.Label(self, text="Summer Semester")
        sumLabel.grid(row=0,column=2)
        self.listBoxes[2].grid(row=1, column=2)

        nextSemesterButton = ttk.Button(self, text="Next Semester", command = self.nextSemester)
        nextSemesterButton.grid(pady=4, row=2,column=2)
        prevSemesterButton = ttk.Button(self, text='Previous Semester', command=self.prevSemester)
        prevSemesterButton.grid(pady=4, row=2,column=0)

        button = ttk.Button(self, text = "Upload DegreeWorks", command = self.getFilePath)
        button.grid(pady=10, row=6, column=1)
        self.fileSelected.label= tk.Label(self,height=2,borderwidth=3,relief="ridge", textvariable = self.fileSelected)
        self.fileSelected.label.grid(row=7, column=1)
        tk.Label(self, text="").grid(row=8, column=1)
        self.CrHours_label= tk.Label(self,text = "Maximum Credit Hours:").grid(row=9, column=1)
        self.CrHours_entry = tk.Entry(self, textvariable= self.CrHours).grid(row=10, column=1)

        button = ttk.Button(self,text = "Generate Schedule",command= self.execute).grid(row=11, column=1)
        button = ttk.Button(self,text= "Quit", command= self.destroy).grid(row=12, column=1)

        
    

    def getFilePath(self):
        self.file = filedialog.askopenfilename(filetypes=[("PDFs","*.pdf")])
        if self.file:
            self.fileSelected.set(os.path.basename(self.file))
        else:
            self.fileSelected.set("No File Selected")

    def nextSemester(self):
        if(self.lastYear):#TODO - Debug msg
            print("debug")
        else:
            self.year += 1
            fallSemesterNum = 3 * (self.year-1)
            sumSemesterNum = (3 * self.year)
            for x in range(fallSemesterNum,sumSemesterNum):
                if(len(self.schedule)<sumSemesterNum):
                    sumSemesterNum = len(self.schedule)-1
                listBox = self.listBoxes[x%3]
                listBox.delete(0, END)
                print(x)
                if(len(self.schedule)<=x):
                    self.lastYear = True
                else:
                    for course in self.schedule[x]:
                        listBox.insert(END, course.CourseNum)
    def prevSemester(self):
        if(self.year<=1): #TODO - give debug message to user
            self.year = 1
        else:
            if(self.lastYear):
                self.lastYear = False
            self.year -= 1
            fallSemesterNum = 3 * (self.year-1)
            sumSemesterNum = (3 * self.year)
            for x in range(fallSemesterNum,sumSemesterNum):
                if(len(self.schedule)<sumSemesterNum):
                    sumSemesterNum = len(self.schedule)-1
                listBox = self.listBoxes[x%3]
                listBox.delete(0, END)
                for course in self.schedule[x]:
                    listBox.insert(END, course.CourseNum)

    def execute(self):
        if self.file:
            parsed = courseParser.getContent(self.file)
            CoursesDict = courseParser.createFromParse(parsed)
            CoursesDict = courseParser.readXL("CPSCXL.xlsx", CoursesDict)
            global globalHoursCount
            globalHoursCount = self.CrHours.get()
            startingSemester = "Fall" # TO DO - add code to get date input for starting semester
            if self.CrHours.get() > 2:
                schedule = scheduler.setSchedule(self.CrHours.get(), startingSemester, CoursesDict)
                self.schedule = schedule
                self.listBoxes[0].delete(0, END)
                self.listBoxes[1].delete(0, END)
                self.listBoxes[2].delete(0, END)

                for x in range(0,3):
                    listBox = self.listBoxes[x]
                    for course in schedule[x]:
                        listBox.insert(END, course.CourseNum)


                
                    
                
            else:
                messagebox.showerror("Error", "Not enough credit hours each semester")
        else:
            messagebox.showerror("Error", "No File Selected")    

window = SmartClassPlanner()

window.mainloop()
#file_path = filedialog.askopenfilename()

