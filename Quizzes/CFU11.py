 	

# *************************************************************************************

from webbrowser import open_new, open_new_tab #Using 'from' instead of 'import' to reduce memory overhead

url1 = input("Please enter the first URL: ") #Will assume that the argument is supposed to be a string

url2 = input("Please enter the second URL: ")

open_new(url1) #Could be either open_new or open_new_tab

open_new_tab(url2) #must be open_new_tab to open in the same window as created in the prior line

# *************************************************************************************

# Import the web browser module: (25 points)
import webbrowser

# Ask user for two URLs:  (25 points)
url_1 = input('Enter a URL site: ')
url_2 = input('Enter a second URL site: ')

# Open the first URL in a new window, and then open the second URL in the same window (new tab):  (40 points)
webbrowser.open_new(url_1)
webbrowser.open_new_tab(url_2)

# Sufficient comments (10 points)