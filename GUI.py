import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import math
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
                self.listBoxes[0].delete(0, END)
                self.listBoxes[1].delete(0, END)
                self.listBoxes[2].delete(0, END)
                i = 0
                rowNum = 1
                for semester in schedule:
                    listBoxInt = i % 3
                    
                    if(listBoxInt == 0 and not(i==0)):
                        
                        rowNum += 1
                        newListBox1 = tk.Listbox()
                        newListBox1.grid(row=rowNum, column=0)
                        newListBox2 = tk.Listbox()
                        newListBox2.grid(row=rowNum, column=1)
                        newListBox3 = tk.Listbox()
                        newListBox3.grid(row=rowNum, column=2)
                        self.listBoxes.append(newListBox1)
                        self.listBoxes.append(newListBox2)
                        self.listBoxes.append(newListBox3)

                        windowHeight = str(500 + ((rowNum-1)*100))
                        self.geometry("500x" + windowHeight)

                    listBox = self.listBoxes[i] #i instead of listBoxInt
                    print(listBox)
                    for course in semester:
                        listBox.insert(END,course.CourseNum)
                    i += 1
                    
                
            else:
                messagebox.showerror("Error", "Not enough credit hours each semester")
        else:
            messagebox.showerror("Error", "No File Selected")    

window = SmartClassPlanner()

window.mainloop()
#file_path = filedialog.askopenfilename()

