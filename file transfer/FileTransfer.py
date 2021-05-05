import shutil
import os 

#source files
source = '/Applications/XAMPP/xamppfiles/htdocs/AJAX_Basics_Project_Files/Python-Projects/file transfer/folderA/'

#destination
destination = '/Applications/XAMPP/xamppfiles/htdocs/AJAX_Basics_Project_Files/Python-Projects/file transfer/folderB/'
files = os.listdir(source)

for i in files:
    shutil.move(source+i, destination)
