#Importing sqlite3 for a relational database
import sqlite3
conn = sqlite3.connect('test1.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_txt(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                col_txtFiles TEXT)")
    conn.commit()

conn = sqlite3.connect('test1.db')

# tuple of files
files_tuple = ('information.docx','Hello.txt','myImage.png', \
               'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

#for loop that loops through each object to find the files that end in .txt
for x in files_tuple:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            #This will indicate a one element tuble for each file ending in .txt
            cur.execute("INSERT INTO tbl_txt (col_txtFiles) VALUES (?)", (x,))
            print(x)

conn.close()
