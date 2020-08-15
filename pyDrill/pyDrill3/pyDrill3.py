import os
import tkinter
from tkinter import *
from tkinter import filedialog
class ParentWindow(Frame):
    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self, master,*args,**kwargs)

        self.master = master
        self.master.resizable(width=False,height=False)
        self.master.geometry('{}x{}'.format(500,175))
        self.master.title('check files')
        self.master.config(bg = 'lightgrey')
        
        self.varFp1 = StringVar()
        self.varFp2 = StringVar()
        
        self.txtFp1 = Entry(self.master, text = self.varFp1, width = 55 )
        self.txtFp1.grid(row = 0, column = 1, rowspan = 1, columnspan = 2, padx = (30,0), pady =(45,0), sticky = W+E)

        self.txtFp2 = Entry(self.master, text = self.varFp2, width = 55)
        self.txtFp2.grid(row = 1, column = 1, rowspan = 1, columnspan = 2, padx = (30,0), pady =(15,0), sticky = W+E)

        self.btnBrowse1 = Button(self.master, text = 'Browse', width= 12, height=1, command = self.setTxt1)                  
        self.btnBrowse1.grid(row= 0 , column = 0, padx =(15,0), pady=( 45,0))
        
        self.btnBrowse2 = Button(self.master, text = 'Browse', width= 12, height=1, command = self.setTxt2)
        self.btnBrowse2.grid(row= 1 , column = 0, padx =(15,0), pady=( 10,0), sticky = NE)
        
        self.btnChk = Button(self.master, text = 'Check for files...', width= 12, height=2, command = self.getFiles)
        self.btnChk.grid(row= 3 , column = 0, padx =(15,0), pady=( 10,0))
        
        
        
        self.btnClose = Button(self.master, text = 'Close Program', width= 12, height=2, command = self.closeApp)
        self.btnClose.grid(row= 3 , column = 2, padx=(0,0), pady=( 15,0),sticky = E)
            
    def getDir(self):
        self.fp = filedialog.askdirectory()
        return self.fp
    def setTxt1(self):
        self.getDir()
        self.txtFp1.delete(0,END)
        self.txtFp1.insert(0,"{}".format(self.fp))
    def setTxt2(self):
        self.getDir()
        self.txtFp2.delete(0,END)
        self.txtFp2.insert(0,"{}".format(self.fp))
    def closeApp(self):
        self.master.destroy()

        
    def getFiles(self):
        gFp1 = self.varFp1.get()
        gFp1 = gFp1.replace("/","\\")
        gFp2 = self.varFp2.get()
        gFp2 = gFp2.replace("/","\\")
        self.aPaths =[]
        self.mTimes = []
       
        if gFp1 != "":
            self.addTxtFiles(gFp1)
        if gFp2 !="":
            self.addTxtFiles(gFp2)
        
        self.sortFiles(self.aPaths,self.
                       mTimes)
           
    def addTxtFiles(self, aFilePath):
        fNames = os.listdir(aFilePath)
        for f in fNames:
            if f.endswith('.txt'):
                nPath = os.path.join(aFilePath,f)
                modTime = os.path.getmtime(nPath)
                self.mTimes.append(modTime)
                self.aPaths.append(nPath)
                print("{} {}".format(nPath,modTime))

    def sortFiles(self, varPaths,varModTimes):
        testmTimes = []
        matchedTest = []
        matchedTime = []
        for t in varModTimes:
             testmTimes.append(t)
             matchedTest.append(False)
             matchedTime.append(False)
        testmTimes.sort()
        indexes = []
        running = True
        
        tIndex = 0
        for t in testmTimes:
            index = 0
            for x in varModTimes:
                if matchedTest[tIndex] == False and matchedTime[index] == False:
                    if t == x:
                        indexes.append(index)
                        matchedTime[index] = True
                        matchedTest[tIndex] = True                                             
                    
                index = index +1
            tIndex =tIndex +1
            
        counter =0
        for i in indexes:
            if counter < len(indexes):
                print(varPaths[i], varModTimes[i])
                counter = counter +1
               
               
                
            
        
if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
