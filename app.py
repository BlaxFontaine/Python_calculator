from tkinter import *

# create basic window
window = Tk()

# window params
window.title("Kalculator")
window.geometry("400x600")

# set app icon
icon = PhotoImage(file="calc.gif")
window.iconphoto(True, icon)

# set background color
window.config(background='#1E1F21')

# content
label_title = Label(window, text="Welcome to Kalculator", font=("Roboto", 20), bg='#1E1F21', fg='#CCA871')
label_title.pack()

one_button = Button(window, text="1", font=("Roboto", 20), bg='#1E1F21', fg='#CCA871')
one_button.pack()
two_button = Button(window, text="2", font=("Roboto", 20), bg='#1E1F21', fg='#CCA871')
two_button.pack()
three_button = Button(window, text="3", font=("Roboto", 20), bg='#1E1F21', fg='#CCA871')
three_button.pack()
four_button = Button(window, text="4", font=("Roboto", 20), bg='#1E1F21', fg='#CCA871')
four_button.pack()
five_button = Button(window, text="5", font=("Roboto", 20), bg='#1E1F21', fg='#CCA871')
five_button.pack()
six_button = Button(window, text="6", font=("Roboto", 20), bg='#1E1F21', fg='#CCA871')
six_button.pack()
seven_button = Button(window, text="7", font=("Roboto", 20), bg='#1E1F21', fg='#CCA871')
seven_button.pack()
eight_button = Button(window, text="8", font=("Roboto", 20), bg='#1E1F21', fg='#CCA871')
eight_button.pack()
nine_button = Button(window, text="9", font=("Roboto", 20), bg='#1E1F21', fg='#CCA871')
nine_button.pack()
zero_button = Button(window, text="0", font=("Roboto", 20), bg='#1E1F21', fg='#CCA871')
zero_button.pack()

# display window
window.mainloop()