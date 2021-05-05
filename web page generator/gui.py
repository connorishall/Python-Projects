import tkinter as tk
import open_html


master = tk.Tk()
tk.Label(master, 
         text="Type in anything").grid(row=0)

def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    htmlCode = "<!DOCTYPE html><html><body><h1> {} </h1></body></html>".format(inp)
    f = open('summer.html', 'w')
    f.write(htmlCode)
    f.close()
    webbrowser.open_new_tab('summer.html')




# TextBox Creation
inputtxt = tk.Text(frame,
                   height = 5,
                   width = 20)
  
inputtxt.pack()
  
#Button Creation
printButton = tk.Button(frame,
                        text = "Submit", 
                        command = lambda:printInput())
printButton.pack()

tk.mainloop()
