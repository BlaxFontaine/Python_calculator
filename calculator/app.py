import parser
import math
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
txtDisplay.insert(0, "")

# Drop down to change bases
tkvar = StringVar(window)
bases = {'Binary', 'Octal', 'Decimal', 'Hexadecimal'}
tkvar.set('Decimal')

popupMenu = OptionMenu(calc, tkvar, *bases)
popupMenu.config(bg='#1E1F21', fg='#CCA871', font=("Courier"))
popupMenu.grid(row=0, column=0)

task = None
# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )
    chosen_base = tkvar.get()
    num = int(float(txtDisplay.get()))
    txtDisplay.delete(0, END)

    if chosen_base == "Binary":
        txtDisplay.insert(0, bin(num)[2:])
    if chosen_base == "Octal":
        txtDisplay.insert(0, int(num, 8))
    if chosen_base == "Decimal":
        txtDisplay.insert(0, int(num, 10))
    if chosen_base == "Hexadecimal":
        txtDisplay.insert(0, hex(num)[2:])

# link function to change dropdown
tkvar.trace('w', change_dropdown)

# function on click
def button_click(num):
    current = txtDisplay.get()
    txtDisplay.delete(0, END)
    txtDisplay.insert(0, current + num)

# clear function
def button_clear():
    txtDisplay.delete(0, END)

def button_operation(op):
    first_num = txtDisplay.get()
    global f_num
    global task
    task = op
    f_num = float(first_num)
    txtDisplay.delete(0, END)

def button_equal():
    second_num = txtDisplay.get()
    txtDisplay.delete(0, END)

    print(type(second_num))

    if task == "add":
        txtDisplay.insert(0, f_num + float(second_num))
    if task == "sub":
        txtDisplay.insert(0, f_num - float(second_num))
    if task == "multi":
        txtDisplay.insert(0, f_num * float(second_num))
    if task == "div":
        txtDisplay.insert(0, f_num / float(second_num))
    if task is None:
        txtDisplay.insert(0, int(float(second_num)))

def button_square():
    sq = float(txtDisplay.get())
    txtDisplay.delete(0, END)
    txtDisplay.insert(0, sq * sq)

def button_math(func):
    num = float(txtDisplay.get())
    txtDisplay.delete(0, END)

    if func == "cos":
        txtDisplay.insert(0, math.cos(num))
    if func == "sin":
        txtDisplay.insert(0, math.sin(num))
    if func == "tan":
        txtDisplay.insert(0, math.tan(num))
    if func == "exp":
        txtDisplay.insert(0, math.exp(num))


def button_pi():
    pi = math.pi
    txtDisplay.delete(0, END)
    txtDisplay.insert(0, pi)

# fill the grid
numberpad = "789456123"
i = 0
btn = []

for j in range(2, 5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2, font=("Courier", 20, "bold"), bg='#1E1F21', fg='#CCA871', bd=1, text=numberpad[i]))
        btn[i].grid(row=j, column= k, pady=1)
        btn[i]["command"]=lambda x=numberpad[i]: button_click(x)
        i+=1

btnClear = Button(calc, text="C", width=6, height=2, font=("Courier", 20, "bold"), bd=1, bg='#1E1F21', fg='#CCA871', command=lambda:button_clear())
btnClear.grid(row=1, column=0, pady=1)

btnAllClear = Button(calc, text="CE", width=6, height=2, font=("Courier", 20, "bold"), bd=1, bg='#1E1F21', fg='#CCA871')
btnAllClear.grid(row=1, column=1, pady=1)

btnSqrRoot = Button(calc, text="√", width=6, height=2, font=("Courier", 20, "bold"), bd=1, bg='#1E1F21', fg='#CCA871')
btnSqrRoot.grid(row=1, column=2, pady=1)

btnAdd = Button(calc, text="+", width=6, height=2, font=("Courier", 20, "bold"), bd=1, bg='#1E1F21', fg='#CCA871', command=lambda:button_operation("add"))
btnAdd.grid(row=1, column=3, pady=1)

btnMinus = Button(calc, text="-", width=6, height=2, font=("Courier", 20, "bold"), bd=1, bg='#1E1F21', fg='#CCA871', command=lambda:button_operation("sub"))
btnMinus.grid(row=2, column=3, pady=1)

btnMulti = Button(calc, text="*", width=6, height=2, font=("Courier", 20, "bold"), bd=1, bg='#1E1F21', fg='#CCA871', command=lambda:button_operation("multi"))
btnMulti.grid(row=3, column=3, pady=1)

btnDivide = Button(calc, text="÷", width=6, height=2, font=("Courier", 20, "bold"), bd=1, bg='#1E1F21', fg='#CCA871', command=lambda:button_operation("div"))
btnDivide.grid(row=4, column=3, pady=1)

btnZero = Button(calc, text="0", width=6, height=2, font=("Courier", 20, "bold"), bd=1, bg='#1E1F21', fg='#CCA871', command=lambda:button_click("0"))
btnZero.grid(row=5, column=0, pady=1)

btnDot = Button(calc, text=".", width=6, height=2, font=("Courier", 20, "bold"), bd=1, bg='#1E1F21', fg='#CCA871')
btnDot.grid(row=5, column=1, pady=1)

btnSqr = Button(calc, text="²", width=6, height=2, font=("Courier", 20, "bold"), bd=1, bg='#1E1F21', fg='#CCA871', command=lambda:button_square())
btnSqr.grid(row=5, column=3, pady=1)

btnEq = Button(calc, text="=", width=6, height=2, font=("Courier", 20, "bold"), bd=1, bg='#CCA871', fg='#1E1F21', command=lambda:button_equal())
btnEq.grid(row=5, column=2, pady=1)

btnPi = Button(calc, text="π", width=6, height=2, font=("Courier", 20, "bold"), bd=1, bg='#1E1F21', fg='#CCA871', command=lambda:button_pi())
btnPi.grid(row=1, column=4, pady=1)

btnSin = Button(calc, text="Sin", width=6, height=2, font=("Courier", 20, "bold"), bd=1, bg='#1E1F21', fg='#CCA871', command=lambda:button_math("sin"))
btnSin.grid(row=1, column=5, pady=1)

btnCos = Button(calc, text="Cos", width=6, height=2, font=("Courier", 20, "bold"), bd=1, bg='#1E1F21', fg='#CCA871', command=lambda:button_math("cos"))
btnCos.grid(row=1, column=6, pady=1)

btnTan = Button(calc, text="Tan", width=6, height=2, font=("Courier", 20, "bold"), bd=1, bg='#1E1F21', fg='#CCA871', command=lambda:button_math("tan"))
btnTan.grid(row=1, column=7, pady=1)

btnExp = Button(calc, text="Exp", width=6, height=2, font=("Courier", 20, "bold"), bd=1, bg='#1E1F21', fg='#CCA871', command=lambda:button_math("exp"))
btnExp.grid(row=2, column=4, pady=1)

btnOpenPar = Button(calc, text="(", width=6, height=2, font=("Courier", 20, "bold"), bd=1, bg='#1E1F21', fg='#CCA871')
btnOpenPar.grid(row=3, column=4, pady=1)

btnClosePar = Button(calc, text="(", width=6, height=2, font=("Courier", 20, "bold"), bd=1, bg='#1E1F21', fg='#CCA871')
btnClosePar.grid(row=4, column=4, pady=1)

# display window
window.mainloop()