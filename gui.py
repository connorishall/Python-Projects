import tkinter as tk
import open_html


master = tk.Tk()
tk.Label(master, 
         text="Type in anything").grid(row=0)


e1 = tk.Entry(master)


e1.grid(row=0, column=1)


tk.Button(master, 
          text='Submit', 
          command = lambda: open_html.test()).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.mainloop()
