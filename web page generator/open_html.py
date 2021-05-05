



import webbrowser
import os
  
# to open/create a new html file in the write mode
def test():
    f = open('summer.html', 'w')
  
# the html code which will go in the file GFG.html
    html_template = """
    <html>
    <head></head>
    <body>
    <h1
    <p>Stay tuned for our amazing summer sale!</p>
    </h1>
    </body>
    </html>
    """
# writing the code into the file
    f.write(html_template)
  
# close the file
    f.close()

    filename = 'file:///'+os.getcwd()+'/' + 'summer.html'
    webbrowser.open_new_tab(filename)
