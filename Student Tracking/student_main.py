


from tkinter import *
import tkinter as tk

import student_gui
import student_func

#This frame is the tkinter frme class that our own class will inherit
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #master configurations
        self.master = master
        self.master.minsize(500,300)
        self.master.configure(bg="#F0F0F0")
        self.master.protocol("WM_DELETE_WINDOW", lambda: student_func.ask_quit(self))
        student_gui.load_gui(self)



if __name__ == "__main__":
    root = tk.TK()
    App = ParentWindow(root)
    root.mainloop()
        
