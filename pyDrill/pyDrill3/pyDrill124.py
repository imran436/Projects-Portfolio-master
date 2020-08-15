import tkinter
from tkinter import filedialog
from tkinter import *
import os
import sqlite3
import sys 
import time
import shutil


class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__ (self, master, *args, **kwargs)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(500,175))

        self.master.title('check files')


        self.txtSource = Entry(self.master, width = 50 )
        self.txtSource.grid(row = 0, column = 1, rowspan = 1, columnspan = 2, padx = (30,0), pady =(45,0), sticky = W+E)

        self.txtDestination = Entry(self.master, width = 50 )
        self.txtDestination.grid(row = 1, column = 1, rowspan = 1, columnspan = 2, padx = (30,0), pady =(15,0), sticky = W+E)

        self.btnSource = Button(self.master, text="Source Directory", width=18, height=1, command=self.sourceDir)
        self.btnSource.grid(row= 0 , column = 0, padx =(15,0), pady=( 45,0))

        self.btnDestination = Button(self.master, text="Destination Directory", width=18, height=1, command=self.destDir)
        self.btnDestination.grid(row= 1 , column = 0, padx =(15,0), pady=( 10,0), sticky = NE)

        self.btnChk = Button(self.master, text="Check for files...", width=18, height=2, command=self.MoveTextFiles)
        self.btnChk.grid(row= 3 , column = 0, padx =(15,0), pady=( 10,0))

        self.btnClose = Button(self.master, text = 'Close Program', width= 12, height=2, command = self.closeApp)
        self.btnClose.grid(row= 3 , column = 2, padx=(0,0), pady=( 15,0),sticky = E)


    def closeApp(self):
        self.master.destroy()
        
    def sourceDir(self):
        self.sfp = filedialog.askdirectory()
        self.txtSource.insert(0,"{}".format(self.sfp))

    def destDir(self):
        self.dfp = filedialog.askdirectory()
        self.txtDestination.insert(0,"{}".format(self.dfp))

    def MoveTextFiles(self):
        for file in os.listdir(self.sfp):
            if file.endswith(".txt"):
                SPath = os.path.join(self.sfp, file)
                self.DPath = shutil.move(SPath, self.dfp)

        conn = sqlite3.connect('FilesDB.db')
        with conn:
            
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS tbl_TxtFiles ( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_FileName STRING, \
                col_MTime)")
            conn.commit()
        conn.close()
        
        for item in os.listdir(self.dfp):
            conn = sqlite3.connect('FilesDB.db')
            with conn:
                cur = conn.cursor()
                if item.endswith('.txt'):
                    abPath = os.path.join(self.dfp, item)
                    time_stamp = os.path.getmtime(abPath)
                    cur.execute("INSERT INTO tbl_TxtFiles(col_FileName, col_Mtime) VALUES (?, ?)", (item, time_stamp,))
                    conn.commit()
        conn.close()
 
        conn = sqlite3.connect('FilesDB.db')
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM tbl_TxtFiles")
            printStuff = cur.fetchall()
            print(printStuff)
        conn.close()
            








if __name__  == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
