import tkinter as tk



master = tk.Tk()
tk.Label(master, 
         text="Type in anything").grid(row=0)


e1 = tk.Entry(master)


e1.grid(row=0, column=1)

tk.Button(master, 
          text='Submit', 
          command=master.quit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.mainloop()
