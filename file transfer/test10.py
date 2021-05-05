import os
import datetime
import shutil

#source files
source = '/Applications/XAMPP/xamppfiles/htdocs/AJAX_Basics_Project_Files/Python-Projects/file transfer/folderA/'

#destination
destination = '/Applications/XAMPP/xamppfiles/htdocs/AJAX_Basics_Project_Files/Python-Projects/file transfer/folderB/'
files = os.listdir(source)

for i in files:
    modeTime = os.path.getmtime(source+i)
    modificationTime = datetime.datetime.fromtimestamp(modeTime)
    twentyfour = datetime.datetime.now() - datetime.timedelta(hours = 24)
    if modificationTime > twentyfour:
        
        shutil.move(source+i, destination)
    
