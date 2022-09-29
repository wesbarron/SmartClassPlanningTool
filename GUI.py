import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import courseParser
import scheduler
import os

class SmartClassPlanner(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SmartClass Planning Tool")
        self.geometry("300x400")
        

        self.file = ""
        self.CrHours= IntVar()
        self.fileSelected= StringVar()
        self.fileSelected.set("No File Selected")
        self.CreateWidgets()

    def CreateWidgets(self):
        
        
        button = ttk.Button(self, text = "Upload DegreeWorks", command = self.getFilePath)
        button.pack(pady = 10)
        self.fileSelected.label= tk.Label(self,height=2,borderwidth=3,relief="ridge", textvariable = self.fileSelected)
        self.fileSelected.label.pack(pady=8)
        tk.Label(self, text="").pack(pady=3)
        self.CrHours_label= tk.Label(self,text = "Maximum Credit Hours:").pack(pady=10)  
        self.CrHours_entry = tk.Entry(self, textvariable= self.CrHours).pack()

        button = ttk.Button(self,text = "Generate Schedule",command= self.execute).pack(pady=50)
        button = ttk.Button(self,text= "Quit", command= self.destroy).pack(side= "bottom")
             

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
            CoursesDict = courseParser.readXL("SmartClassPlanningTool-main\CPSCXL.xlsx", CoursesDict)
            if self.CrHours.get() > 2:
                scheduler.setSchedule(self.CrHours.get(), CoursesDict)
            else:
                messagebox.showerror("Error", "Not enough credit hours each semester") 
        else:
            messagebox.showerror("Error", "No File Selected")    



window = SmartClassPlanner()

window.mainloop()
#file_path = filedialog.askopenfilename()

