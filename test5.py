import tkinter as tk
import webbrowser

# Top level window
frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('400x200')
# Function for getting Input
# from textbox and printing it 
# at label widget
  
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
# Label Creation
lbl = tk.Label(frame, text = "")
lbl.pack()
frame.mainloop()
