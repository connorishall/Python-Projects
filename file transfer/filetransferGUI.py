import tkinter as tk
    

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="test", 
                   fg="red", )
button.pack(side=tk.LEFT)

button = tk.Button(frame, 
                   text="test", 
                   fg="blue", )
button.pack(side=tk.LEFT)

button = tk.Button(frame, 
                   text="test", 
                   fg="green", )
button.pack(side=tk.LEFT)

root.mainloop()
