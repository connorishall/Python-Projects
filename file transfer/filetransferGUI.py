import tkinter as tk
    



self.txt_browser1 = tk.Entry(self.master,text='',width=70)
self.txt_browser1.grid(row=0,column=2,rowspan=1,columnspan=1,padx=(30,40),pady(40,0),sticky=N+W)
self.txt_browser2 = tk.Entry(self.master,text='',width=70)
self.txt_browser2.grid(row=1,column=2,rowspan=1,columnspan=1,padx=(30,40),pady(0,0),sticky=N+W)



self.btn_add = tk.Button(self.master,width=12,height=1,text='Browse..',command=lambda: drill3_func.browser(self))
self.btn_add.grid(row=0,column=1,padx=(5,0),pady=(40,0),sticky=W)
self.btn_add = tk.Button(self.master,width=12,height=1,text='Browse..',command=lambda: drill3_func.browser2(self))
self.btn_add.grid(row=1,column=1,padx=(5,0),pady=(5,0),sticky=W)
self.btn_add = tk.Button(self.master,width=12,height=2,text='Check for files...',command=lambda: drill3_func.checkfile(self))
self.btn_add.grid(row=2,column=1,padx=(5,0),pady=(5,0),sticky=W)
self.btn_add = tk.Button(self.master,width=12,height=2,text='Close Program',command=lambda: drill3_func.ask_quit(self))
self.btn_add.grid(row=2,column=2,padx=(5,0),pady=(5,0),sticky=E)

root.mainloop()
