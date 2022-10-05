

import re
global run
run = True

def performmath():
    #global run
    equation = input("Enter equation")
    if equation == 'quit':
        run = False
    else:
        print("You types", equation)

while run:
    performmath()