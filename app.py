import parser
from tkinter import *

# create basic window
window = Tk()

# window params
window.title("Kalculator")
window.geometry("1000x468+0+0")

# set app icon
icon = PhotoImage(file="calc.gif")
window.iconphoto(True, icon)

# set background color
window.config(background='#1E1F21')

# content

calc = Frame(window, bg='#1E1F21')
calc.grid()

# label_title = Label(calc, text="Welcome to Kalculator", font=("Courier", 20), bg='#1E1F21', fg='#CCA871')
# label_title.grid()

txtDisplay = Entry(calc, font=("Courier", 20, "bold"), bg='#1E1F21', fg='#CCA871', bd=20, width=28, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=9, pady=1)
txtDisplay.insert(0, "0")

def button_click(num):
    # num = int(num)
    txtDisplay.delete(0, END)
    txtDisplay.insert(0, num)


numberpad = "789456123"
i = 0
btn = []

for j in range(2, 5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2, font=("Courier", 20, "bold"), bg='#1E1F21', fg='#CCA871', bd=1, text=numberpad[i]))
        btn[i].grid(row=j, column= k, pady=1)
        btn[i]["command"]=lambda x=numberpad[i]: button_click(x)
        i+=1

btnClear = Button(calc, text="C", width=6, height=2, font=("Courier", 20, "bold"), bd=1, bg='#1E1F21', fg='#CCA871')
btnClear.grid(row=1, column=0, pady=1)

btnAllClear = Button(calc, text="CE", width=6, height=2, font=("Courier", 20, "bold"), bd=1, bg='#1E1F21', fg='#CCA871')
btnAllClear.grid(row=1, column=1, pady=1)

btnSqrRoot = Button(calc, text="√", width=6, height=2, font=("Courier", 20, "bold"), bd=1, bg='#1E1F21', fg='#CCA871')
btnSqrRoot.grid(row=1, column=2, pady=1)

btnAdd = Button(calc, text="+", width=6, height=2, font=("Courier", 20, "bold"), bd=1, bg='#1E1F21', fg='#CCA871')
btnAdd.grid(row=1, column=3, pady=1)

btnMinus = Button(calc, text="-", width=6, height=2, font=("Courier", 20, "bold"), bd=1, bg='#1E1F21', fg='#CCA871')
btnMinus.grid(row=2, column=3, pady=1)

btnTimes = Button(calc, text="*", width=6, height=2, font=("Courier", 20, "bold"), bd=1, bg='#1E1F21', fg='#CCA871')
btnTimes.grid(row=3, column=3, pady=1)

btnDivide = Button(calc, text="÷", width=6, height=2, font=("Courier", 20, "bold"), bd=1, bg='#1E1F21', fg='#CCA871')
btnDivide.grid(row=4, column=3, pady=1)

btnZero = Button(calc, text="0", width=6, height=2, font=("Courier", 20, "bold"), bd=1, bg='#1E1F21', fg='#CCA871')
btnZero.grid(row=5, column=0, pady=1)

btnDot = Button(calc, text=".", width=6, height=2, font=("Courier", 20, "bold"), bd=1, bg='#1E1F21', fg='#CCA871')
btnDot.grid(row=5, column=1, pady=1)

btnSqr = Button(calc, text="²", width=6, height=2, font=("Courier", 20, "bold"), bd=1, bg='#1E1F21', fg='#CCA871')
btnSqr.grid(row=5, column=3, pady=1)

btnEq = Button(calc, text="=", width=6, height=2, font=("Courier", 20, "bold"), bd=1, bg='#CCA871', fg='#1E1F21')
btnEq.grid(row=5, column=2, pady=1)

btnPi = Button(calc, text="π", width=6, height=2, font=("Courier", 20, "bold"), bd=1, bg='#1E1F21', fg='#CCA871')
btnPi.grid(row=1, column=4, pady=1)

btnSin = Button(calc, text="Sin", width=6, height=2, font=("Courier", 20, "bold"), bd=1, bg='#1E1F21', fg='#CCA871')
btnSin.grid(row=1, column=5, pady=1)

btnCos = Button(calc, text="Cos", width=6, height=2, font=("Courier", 20, "bold"), bd=1, bg='#1E1F21', fg='#CCA871')
btnCos.grid(row=1, column=6, pady=1)

btnTan = Button(calc, text="Tan", width=6, height=2, font=("Courier", 20, "bold"), bd=1, bg='#1E1F21', fg='#CCA871')
btnTan.grid(row=1, column=7, pady=1)


# display window
window.mainloop()