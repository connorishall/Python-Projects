import os
filename = "/Applications/XAMPP/xamppfiles/htdocs/AJAX_Basics_Project_Files/Python-Projects/file transfer/folderB/"
statbuf = os.stat(filename)
print("Modification time: {}".format(statbuf.st_mtime))
